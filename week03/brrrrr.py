import chess
import chess.engine
from collections import defaultdict
import os
import time
import requests
import re
import csv
import statistics
import random

# ---- CONFIG ----
OP_TOKEN = os.environ.get("OP_TOKEN")
STOCKFISH_PATH = "/Users/salvador.dali.disciple/homebrew/bin/stockfish"
engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

# ---- SYSTEM PROMPT ----
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

# ---- LOAD PUZZLES ----
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
{puzzle["pgn"]}
</PGN>

<UCI>
{puzzle["uci"]}
</UCI>
</question>
""".strip()

# ---- MODEL CALL ----
def call_model(system_prompt: str, model_name: str, query_prompt: str,
               temp: float, top_p: float, max_tokens: int):
    prompt = build_system_prompt(max_tokens)
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OP_TOKEN}",
                "Content-Type": "application/json"
            },
            json={
                "model": model_name,
                "messages": [
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": query_prompt}
                ],
                "max_tokens": max_tokens,
                "temperature": temp,
                "top_p": top_p,
                "include_reasoning": False,
            }
        )
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content'].strip()
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"

# ---- EVALUATION ----
def normalize_stockfish_0_1(eval_str, max_cp=1000, invalid_val=0.0):
    if not eval_str:
        return invalid_val
    eval_str = eval_str.strip()
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
    return invalid_val

def clean_move_str(move_str: str) -> str:
    move_str = move_str.strip()
    move_str = re.sub(r'<[^>]+>', '', move_str)
    move_str = move_str.replace("**", "").replace("*", "").replace("__", "").replace("_", "")
    move_str = re.sub(r"[+#]", "", move_str)
    move_str = re.sub(r"^\d+\.\s*", "", move_str)
    move_str = re.sub(r"\([^)]*\)", "", move_str)
    move_str = re.sub(r'^[^\w]*|[^\w]*$', '', move_str)
    return move_str

def parse_and_evaluate(move_str: str, board: chess.Board):
    move_str = clean_move_str(move_str)
    result = {"move": move_str, "uci": None, "legal": False, "eval": None, "fen": board.fen()}
    try:
        move = board.parse_san(move_str)
        board.push(move)
        result["uci"] = move.uci()
        result["legal"] = True
        result["fen"] = board.fen()
    except Exception:
        result["legal"] = False
        return result
    info = engine.analyse(board, chess.engine.Limit(depth=15))
    score = info["score"]
    if score.is_mate():
        result["eval"] = f"Mate in {score.white().mate()}"
    else:
        cp = score.white().score(mate_score=100000)
        result["eval"] = f"{cp} cp"
    return result

# ---- SAVE RESULTS ----
def save_results_csv(results, system_prompt_path, model, tmp, top_p, max_tokens, puzzle_id):
    results_dir = "gpt-temp-check"
    os.makedirs(results_dir, exist_ok=True)
    system_name = os.path.splitext(os.path.basename(system_prompt_path))[0]
    filename = os.path.join(
        results_dir,
        f"res_{system_name}_{model.replace('/', '-')}_T{tmp}_P{top_p}_M{max_tokens}_Puzzle{puzzle_id}.csv"
    )

    norm_values = []
    legal_norms = []
    illegal_count = 0
    total_count = 0
    legal_moves_seen = []

    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["Call#", "PuzzleID", "Move", "Legal", "UCI", "Eval",
                      "Normalized", "FEN", "Temperature", "Top_p", "Max_tokens"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for idx, res in enumerate(results, start=1):
            move_val = res['move']
            if len(move_val) > 10:
                move_val = "SE"
            norm_val = normalize_stockfish_0_1(res.get('eval', ''))
            writer.writerow({
                "Call#": idx,
                "PuzzleID": puzzle_id,
                "Move": move_val,
                "Legal": res['legal'],
                "UCI": res.get('uci', ''),
                "Eval": res.get('eval', ''),
                "Normalized": round(norm_val, 3),
                "FEN": res.get("fen", ""),
                "Temperature": tmp,
                "Top_p": top_p,
                "Max_tokens": max_tokens
            })
            norm_values.append(norm_val)
            total_count += 1
            if res['legal']:
                legal_norms.append(norm_val)
                legal_moves_seen.append(move_val)
            else:
                illegal_count += 1

        mean_val = statistics.mean(norm_values) if norm_values else 0.0
        std_val = statistics.pstdev(norm_values) if len(norm_values) > 1 else 0.0
        mae_val = statistics.mean(abs(v - 0.5) for v in norm_values) if norm_values else 0.0
        illegal_pct = (illegal_count / total_count * 100) if total_count > 0 else 0.0
        legal_mean = statistics.mean(legal_norms) if legal_norms else 0.0

        move_freq = {}
        for mv in legal_moves_seen:
            move_freq[mv] = move_freq.get(mv, 0) + 1
        most_freq_move, most_freq_count = (None, 0)
        if move_freq:
            most_freq_move, most_freq_count = max(move_freq.items(), key=lambda x: x[1])
            most_freq_pct = most_freq_count / total_count * 100
        else:
            most_freq_pct = 0.0

        writer.writerow({})
        writer.writerow({"Move": "=== Summary Statistics ==="})
        writer.writerow({"Move": "Puzzle ID", "Eval": puzzle_id})
        writer.writerow({"Move": "Average Normalized Value", "Eval": round(mean_val, 3)})
        writer.writerow({"Move": "Standard Deviation", "Eval": round(std_val, 3)})
        writer.writerow({"Move": "Mean Absolute Error (from 0.5)", "Eval": round(mae_val, 3)})
        writer.writerow({"Move": "Illegal Moves (%)", "Eval": f"{illegal_pct:.2f}%"})
        writer.writerow({"Move": "Mean Value (Legal Moves Only)", "Eval": round(legal_mean, 3)})
        writer.writerow({"Move": "Unique Legal Moves", "Eval": len(move_freq)})
        writer.writerow({"Move": "Most Frequent Move", "Eval": f"{most_freq_move} ({most_freq_pct:.1f}%)"})
        writer.writerow({"Move": "Temperature", "Eval": tmp})
        writer.writerow({"Move": "Top_p", "Eval": top_p})
        writer.writerow({"Move": "Max_tokens", "Eval": max_tokens})

    print(f"\n✅ Results saved to {filename}")

# ---- MAIN ----
class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    END = '\033[0m'

if __name__ == "__main__":
    models = [
        "openai/gpt-4.1-mini",
        "deepseek/deepseek-chat-v3.1"
    ]
    temper = [0.0,
              0.1,
              0.2,
              0.3,
              0.4,
              0.5,
              0.6,
              0.7,
              0.8,
              0.9,
              1
              ]
    top_ps = [0.3]
    max_tokens = 1000
    system_prompt_file = "./system_prompts/base.txt"
    puzzles = load_pickpocket("pickpocket_after_breakage.txt")
    num_calls = 100  # run 100 calls per puzzle/temp for stats

    for puzzle in puzzles:
        fen = puzzle["fen"]
        query_prompt = build_prompt_from_puzzle(puzzle)
        for tmp in temper:
            for top_p in top_ps:
                print(f"\n=== Temp {Color.RED}{tmp}{Color.END} | Top_p {Color.RED}{top_p}{Color.END} | Max tokens {Color.RED}{max_tokens}{Color.END} | Puzzle {puzzle['id']} ===")
                for model in models:
                    results = []
                    print(f"\nTesting {Color.RED}{model}{Color.END}...")
                    for call_num in range(num_calls):
                        board = chess.Board(fen)
                        response = call_model(system_prompt_file, model, query_prompt, tmp, top_p, max_tokens)
                        move_response = response.split("\n")[0].strip()
                        move_result = parse_and_evaluate(move_response, board)
                        move_result["fen"] = fen
                        results.append(move_result)
                        print(f"  Call {call_num+1}: Move={move_result['move']} | Legal={move_result['legal']} | Eval={move_result['eval']}")
                        time.sleep(1)
                    save_results_csv(results, system_prompt_file, model, tmp, top_p, max_tokens, puzzle["id"])

    engine.quit()
