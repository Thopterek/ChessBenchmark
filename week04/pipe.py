#!/usr/bin/env python3
"""
Updated pipeline - preserves your original logic and adds:
- Puzzle Solving Accuracy (exact SAN match)
- Move Quality (Stockfish eval -> normalized)
- Instruction Adherence (illegal move rate)
- Efficiency (OpenRouter usage: prompt/completion/total tokens, cost) + latency

Saves results for one run (model/temp/top_p/max_tokens) into a single CSV per run,
and appends summary statistics at the end of that CSV.

Make sure:
- OP_TOKEN environment variable is set (OpenRouter API key).
- STOCKFISH_PATH points to your stockfish binary.
- pickpocket.txt is in the working directory (same format you provided).
"""

import os
import time
import re
import csv
import json
import requests
import statistics
import chess
import chess.engine

# ---- CONFIG ----
OP_TOKEN = os.environ.get("OP_TOKEN")  # OpenRouter key (same as before)
STOCKFISH_PATH = "/Users/salvador.dali.disciple/homebrew/bin/stockfish"  # adjust if needed
engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# ---- SYSTEM PROMPT (kept as you had it) ----
def build_system_prompt(max_tokens: int) -> str:
    input_budget = int(max_tokens * 0.2)
    reasoning_budget = int(max_tokens * 0.6)
    output_budget = max_tokens - input_budget - reasoning_budget

    return f"""You are a world-class chess grandmaster.

- You will be given:
  - The current board position in FEN notation.
  - A partially completed game history (moves played so far PGN and UCI).

- Your task:
  - Choose the single best next move for the player to move.
  - Output **only the move** in SAN
  - NEVER output explanations, commentary, or reasoning.

- Constraints:
  - Output exactly one move per query.
  - Do not include punctuation, quotes, or extra text.

- Max tokens {max_tokens}:
    - {input_budget} for input
    - {reasoning_budget} for reasoning
    - {output_budget} for output
""".strip()

# ---- LOAD PUZZLES (unchanged) ----
def load_pickpocket(file_path="pickpocket.txt"):
    puzzles = []
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    blocks = content.split("Puzzle ID :")
    for block in blocks[1:]:
        lines = block.strip().splitlines()
        puzzle = {}
        puzzle["id"] = lines[0].strip()
        for l in lines:
            if l.startswith("Rating"):
                puzzle["rating"] = l.split(":")[-1].strip()
            if l.startswith("FEN"):
                puzzle["fen"] = l.split(":", 1)[-1].strip()
            if l.startswith("PGN"):
                puzzle["pgn"] = l.split(":", 1)[-1].strip()
            if l.startswith("UCI"):
                puzzle["uci"] = l.split(":", 1)[-1].strip()
            if l.startswith("Answer SAN"):
                puzzle["answer_san"] = l.split(":", 1)[-1].strip()
            if l.startswith("Answer UCI"):
                puzzle["answer_uci"] = l.split(":", 1)[-1].strip()
        puzzles.append(puzzle)
    return puzzles

def build_prompt_from_puzzle(puzzle):
    return f"""
<question>
<FEN>
{puzzle["fen"]}
</FEN>

<PGN>
{puzzle.get("pgn","")}
</PGN>

<UCI>
{puzzle.get("uci","")}
</UCI>
</question>
""".strip()

# ---- CLEAN / NORMALIZE etc. (kept) ----
def normalize_stockfish_0_1(eval_str, max_cp=1000, invalid_val=0.0):
    if not eval_str:
        return invalid_val
    eval_str = str(eval_str).strip()
    mate_match = re.match(r"Mate in (-?\d+)", eval_str)
    if mate_match:
        mate_in = int(mate_match.group(1))
        if mate_in >= 0:
            if mate_in == 0:
                return 1.0
            else:
                return max(0.91, 1.0 - 0.01 * mate_in)
        else:
            return 0.1
    cp_match = re.match(r"(-?\d+)\s*cp", eval_str)
    if cp_match:
        cp = int(cp_match.group(1))
        cp = max(-max_cp, min(cp, max_cp))
        return 0.5 + (cp / (2 * max_cp)) * 0.8
    # If engine returns score as int (centipawns) handle that:
    try:
        cp = int(eval_str)
        cp = max(-max_cp, min(cp, max_cp))
        return 0.5 + (cp / (2 * max_cp)) * 0.8
    except Exception:
        return invalid_val

def clean_move_str(move_str: str) -> str:
    if move_str is None:
        return ""
    move_str = move_str.strip()
    move_str = re.sub(r'<[^>]+>', '', move_str)
    move_str = move_str.replace("**", "").replace("*", "").replace("__", "").replace("_", "")
    move_str = re.sub(r"[+#]", "", move_str)
    move_str = re.sub(r"^\d+\.\s*", "", move_str)
    move_str = re.sub(r"\([^)]*\)", "", move_str)
    move_str = re.sub(r'^[^\w\-\+]*|[^\w\-\+]*$', '', move_str)
    return move_str

# ---- MODEL CALL (adds usage include + latency) ----
def call_model(system_prompt: str, model_name: str, query_prompt: str,
               temp: float, top_p: float, max_tokens: int,
               retries: int = 2):
    prompt = build_system_prompt(max_tokens)
    headers = {
        "Authorization": f"Bearer {OP_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": query_prompt}
        ],
        "max_tokens": max_tokens,
        "temperature": temp,
        "top_p": top_p,
        "include_reasoning": False,
        "usage": {"include": True}
    }

    for attempt in range(1, retries + 1):
        start_t = time.time()
        try:
            response = requests.post(
                OPENROUTER_URL, headers=headers, json=payload, timeout=120
            )
        except Exception as e:
            if attempt == retries:
                return {"error": f"Request exception: {e}", "latency": time.time() - start_t}
            time.sleep(2)
            continue

        latency = time.time() - start_t

        # Non-200 HTTP code
        if response.status_code != 200:
            err_text = response.text[:500].replace("\n", " ")
            if attempt == retries:
                return {"error": f"HTTP {response.status_code}: {err_text}", "latency": latency}
            time.sleep(2)
            continue

        # Try parsing JSON safely
        try:
            data = response.json()
        except json.JSONDecodeError:
            err_snippet = response.text[:500].replace("\n", " ")
            if attempt == retries:
                return {
                    "error": f"Invalid JSON from API (attempt {attempt}): {err_snippet}",
                    "latency": latency
                }
            time.sleep(2)
            continue

        # Extract text and usage safely
        content = ""
        try:
            content = data["choices"][0]["message"]["content"].strip()
        except Exception:
            if "choices" in data and data["choices"]:
                content = str(data["choices"][0])
            else:
                content = ""

        return {
            "text": content,
            "usage": data.get("usage", {}),
            "id": data.get("id"),
            "latency": latency
        }

    # Should never reach here
    return {"error": "Failed after retries", "latency": None}


# ---- EVALUATION: parse original parse_and_evaluate but extended to compute 'correct' and normalized ----
def parse_and_evaluate(move_str: str, board: chess.Board, answer_san: str = None):
    move_str = clean_move_str(move_str)
    result = {"move": move_str, "uci": None, "legal": False, "eval": None, "fen": board.fen(), "normalized": None, "correct": False}
    if not move_str:
        return result
    try:
        move = board.parse_san(move_str)
        board.push(move)
        result["uci"] = move.uci()
        result["legal"] = True
        result["fen"] = board.fen()
    except Exception:
        # illegal / unparsable SAN
        result["legal"] = False
        return result

    # engine analysis on the new position (after move)
    try:
        info = engine.analyse(board, chess.engine.Limit(depth=15))
        score = info.get("score")
        # chess library Score object handling
        if hasattr(score, "is_mate") and score.is_mate():
            # positive mate -> good for side to move (white perspective). we'll use Score.white().mate()
            try:
                mate_in = score.white().mate()
                result["eval"] = f"Mate in {mate_in}"
            except Exception:
                result["eval"] = "Mate"
        else:
            try:
                cp = score.white().score(mate_score=100000)
                result["eval"] = f"{cp} cp"
            except Exception:
                # fallback if score is a number
                result["eval"] = str(score)
    except Exception as e:
        result["eval"] = None

    # normalized value (0..1) using your normalization
    result["normalized"] = normalize_stockfish_0_1(result.get("eval", ""))

    # correctness check (exact SAN match). Clean both sides to be robust to trailing +/#.
    if answer_san:
        if clean_move_str(answer_san) and clean_move_str(answer_san) == move_str:
            result["correct"] = True
        else:
            result["correct"] = False

    return result

# ---- SAVE RESULTS (single CSV for the whole run) ----
def save_results_csv(results, system_prompt_path, model, tmp, top_p, max_tokens, out_dir="a_test"):
    os.makedirs(out_dir, exist_ok=True)
    system_name = os.path.splitext(os.path.basename(system_prompt_path))[0] if system_prompt_path else "system"
    filename = os.path.join(
        out_dir,
        f"res_{system_name}_{model.replace('/', '-')}_T{tmp}_P{top_p}_M{max_tokens}.csv"
    )

    fieldnames = [
        "Call#", "PuzzleID", "Move", "Correct", "Legal", "UCI", "Eval",
        "Normalized", "FEN", "Latency_s", "Prompt_tokens", "Completion_tokens",
        "Total_tokens", "Cost", "Temperature", "Top_p", "Max_tokens"
    ]

    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        norm_values = []
        legal_norms = []
        illegal_count = 0
        total_count = 0
        correct_count = 0
        latencies = []
        tokens_list = []
        cost_list = []

        for idx, res in enumerate(results, start=1):
            move_val = res.get('move', '')
            if len(move_val) > 40:
                # prevent overly long text in the cell; keep first part
                move_val = move_val[:40] + "..."

            usage = res.get("usage", {}) or {}
            prompt_t = usage.get("prompt_tokens")
            completion_t = usage.get("completion_tokens")
            total_t = usage.get("total_tokens")
            cost = usage.get("cost")

            norm_val = res.get('normalized', 0.0) if res.get('normalized') is not None else 0.0

            writer.writerow({
                "Call#": idx,
                "PuzzleID": res.get("puzzle_id"),
                "Move": move_val,
                "Correct": bool(res.get("correct", False)),
                "Legal": bool(res.get("legal", False)),
                "UCI": res.get("uci", ""),
                "Eval": res.get("eval", ""),
                "Normalized": round(norm_val, 3) if norm_val is not None else "",
                "FEN": res.get("fen", ""),
                "Latency_s": round(res.get("latency", 0.0), 3),
                "Prompt_tokens": prompt_t,
                "Completion_tokens": completion_t,
                "Total_tokens": total_t,
                "Cost": cost,
                "Temperature": tmp,
                "Top_p": top_p,
                "Max_tokens": max_tokens
            })

            # collect stats
            total_count += 1
            if not res.get("legal", False):
                illegal_count += 1
            if res.get("correct", False):
                correct_count += 1
            if res.get("normalized") is not None:
                norm_values.append(res.get("normalized"))
            if res.get("legal", False) and res.get("normalized") is not None:
                legal_norms.append(res.get("normalized"))
            if res.get("latency") is not None:
                latencies.append(res.get("latency"))
            if total_t is not None:
                tokens_list.append(total_t)
            if cost is not None:
                try:
                    cost_list.append(float(cost))
                except Exception:
                    pass

        # summary
        mean_val = round(statistics.mean(norm_values), 4) if norm_values else 0.0
        std_val = round(statistics.pstdev(norm_values), 4) if len(norm_values) > 1 else 0.0
        mae_val = round(statistics.mean(abs(v - 0.5) for v in norm_values), 4) if norm_values else 0.0
        illegal_pct = round((illegal_count / total_count * 100) if total_count > 0 else 0.0, 3)
        accuracy_pct = round((correct_count / total_count * 100) if total_count > 0 else 0.0, 3)
        legal_mean = round(statistics.mean(legal_norms), 4) if legal_norms else 0.0
        avg_latency = round(statistics.mean(latencies), 4) if latencies else None
        avg_tokens = round(statistics.mean(tokens_list), 2) if tokens_list else None
        total_cost = round(sum(cost_list), 6) if cost_list else None
        avg_cost = round(statistics.mean(cost_list), 6) if cost_list else None

        # blank row, then summary rows
        writer.writerow({})
        writer.writerow({"Call#": "=== Summary Statistics ==="})
        writer.writerow({"Call#": "Average Normalized Value", "Eval": mean_val})
        writer.writerow({"Call#": "Standard Deviation", "Eval": std_val})
        writer.writerow({"Call#": "Mean Absolute Error (from 0.5)", "Eval": mae_val})
        writer.writerow({"Call#": "Illegal Moves (%)", "Eval": f"{illegal_pct}%"})
        writer.writerow({"Call#": "Puzzle Solving Accuracy (%)", "Eval": f"{accuracy_pct}%"})
        writer.writerow({"Call#": "Mean Value (Legal Moves Only)", "Eval": legal_mean})
        writer.writerow({"Call#": "Average Latency (s)", "Eval": avg_latency})
        writer.writerow({"Call#": "Average Tokens (total)", "Eval": avg_tokens})
        writer.writerow({"Call#": "Total Cost", "Eval": total_cost})
        writer.writerow({"Call#": "Average Cost per Call", "Eval": avg_cost})
        writer.writerow({"Call#": "Temperature", "Eval": tmp})
        writer.writerow({"Call#": "Top_p", "Eval": top_p})
        writer.writerow({"Call#": "Max_tokens", "Eval": max_tokens})

    print(f"\n✅ Results saved to {filename}")
    return filename

# ---- MAIN (keeps your existing main loop behavior, but collects into one results list per model-run) ----
if __name__ == "__main__":
    models = [
        "x-ai/grok-4",
        "openai/gpt-5",
        "anthropic/claude-opus-4.1",
        "google/gemini-2.5-pro",
        "deepseek/deepseek-chat",
        "mistralai/mistral-medium-3.1"
    ]
    temper = [0.0]      # keep your setting
    top_ps = [1]        # keep your setting
    max_tokens = 4096
    system_prompt_file = "./system_prompts/base.txt"
    puzzles = load_pickpocket("pickpocket.txt")
    num_calls = 1    # keep your choice

    # NOTE: per your note, you'll likely call only one model / one temp / one top_p per run;
    # this loop still supports iterating multiple models if you want.
    for model in models:
        for tmp in temper:
            for top_p in top_ps:
                print(f"\n=== Run: model={model} | temp={tmp} | top_p={top_p} | max_tokens={max_tokens} ===")
                all_results = []  # collect across puzzles & calls
                call_global_idx = 0

                for puzzle in puzzles:
                    fen = puzzle["fen"]
                    query_prompt = build_prompt_from_puzzle(puzzle)
                    answer_san = puzzle.get("answer_san", "").strip()

                    for call_num in range(num_calls):
                        call_global_idx += 1
                        board = chess.Board(fen)
                        # model call
                        model_resp = call_model(system_prompt_file, model, query_prompt, tmp, top_p, max_tokens)
                        if "error" in model_resp:
                            print(f"Call {call_global_idx}: ERROR - {model_resp['error']}")
                            move_text = model_resp.get("error", "")
                            usage = model_resp.get("usage", {})
                            latency = model_resp.get("latency", None)
                            move_result = {
                                "puzzle_id": puzzle["id"],
                                "move": move_text,
                                "uci": None,
                                "legal": False,
                                "eval": None,
                                "normalized": None,
                                "correct": False,
                                "fen": fen,
                                "usage": usage,
                                "latency": latency
                            }
                            all_results.append(move_result)
                            # small sleep to be polite / avoid rate limits
                            time.sleep(1)
                            continue

                        move_text = model_resp.get("text", "")
                        usage = model_resp.get("usage", {}) or {}
                        latency = model_resp.get("latency", None)

                        # parse and evaluate
                        # we pass a fresh board because parse_and_evaluate will push move
                        board_for_eval = chess.Board(fen)
                        parsed = parse_and_evaluate(move_text, board_for_eval, answer_san)

                        # merge usage & latency
                        parsed["usage"] = usage
                        parsed["latency"] = latency
                        parsed["puzzle_id"] = puzzle["id"]

                        all_results.append(parsed)

                        print(f"  Call {call_global_idx}: Puzzle={puzzle['id']} Move='{parsed['move']}' Legal={parsed['legal']} Correct={parsed['correct']} Eval={parsed['eval']} Latency={round(latency,3) if latency else None}")

                        # rate limit politeness
                        time.sleep(1)

                # save aggregated CSV for this model/temp/top_p run
                save_results_csv(all_results, system_prompt_file, model, tmp, top_p, max_tokens)

    engine.quit()
