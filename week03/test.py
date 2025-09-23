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

OP_TOKEN = os.environ.get("OP_TOKEN")

# ---- STOCKFISH SETUP ----
STOCKFISH_PATH = "/Users/salvador.dali.disciple/homebrew/bin/stockfish"
engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)


# ---- MODEL CALL FUNCTION ----
def call_model(system_prompt: str, model_name: str, query_prompt: str, temp: float):
    try:
        with open(system_prompt, 'r', encoding='utf-8') as file:
            sys_prompt = file.read().strip()
    except FileNotFoundError:
        return "Error: System prompt file not found"
    
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
                    {"role": "system", "content": sys_prompt},
                    {"role": "user", "content": query_prompt}
                ],
                "max_tokens": 1000,
                "temperature": temp,
                "include_reasoning": False
            }
        )
        
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content'].strip()
        else:
            return f"Error: {response.status_code} - {response.text}"
            
    except Exception as e:
        return f"Error: {str(e)}"


# ---- NORMALIZATION ----
def normalize_stockfish_0_1(eval_str, max_cp=1000, invalid_val=0.0):
    """
    Normalize Stockfish eval string to [0.0, 1.0].
    - invalid (syntax error / no move) → 0.0
    - losing mate (Mate in -N) → 0.1
    - centipawn scores: scaled into [0.1, 0.9]
    - winning mate (Mate in +N): scaled into (0.9, 1.0]
    """
    if not eval_str:
        return invalid_val  # invalid / missing

    eval_str = eval_str.strip()

    # Mate
    mate_match = re.match(r"Mate in (-?\d+)", eval_str)
    if mate_match:
        mate_in = int(mate_match.group(1))
        if mate_in > 0:  # winning mate
            return min(1.0, 0.9 + 0.01 * (1.0 / mate_in))
        else:            # losing mate
            return 0.1

    # Centipawns
    cp_match = re.match(r"(-?\d+)\s*cp", eval_str)
    if cp_match:
        cp = int(cp_match.group(1))
        cp = max(-max_cp, min(cp, max_cp))  # clamp
        # map -max_cp → 0.1, 0 → 0.5, +max_cp → 0.9
        return 0.5 + (cp / (2 * max_cp)) * 0.8

    # If unknown eval
    return invalid_val


# ---- FEN UTILITIES ----
def load_fens(fen_file="391k-valid.fen"):
    with open(fen_file, "r") as f:
        fens = [line.strip() for line in f if line.strip()]
    return fens

def fen_to_ascii_board(fen):
    board = chess.Board(fen)
    output = []
    for rank in range(8, 0, -1):
        row = []
        for file in range(8):
            square = chess.square(file, rank-1)
            piece = board.piece_at(square)
            row.append(piece.symbol() if piece else ".")
        output.append(f"{rank}  " + "  ".join(row))
    output.append("   " + "  ".join("abcdefgh"))
    return "\n".join(output)

def build_prompt_from_fen(fen):
    ascii_board = fen_to_ascii_board(fen)
    return f"""
<question>Based on the board provided below:
Find the best possible move for the white player.

<FEN>
{fen}
</FEN>

<BOARD>
{ascii_board}
</BOARD>

<answer>
Formulate the answer as just one move.
Use algebraic notation.
</answer>
</question>
""".strip()


# ---- CLEAN + PARSE ----
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

    # Stockfish evaluation
    info = engine.analyse(board, chess.engine.Limit(depth=15))
    score = info["score"]

    if score.is_mate():
        result["eval"] = f"Mate in {score.white().mate()}"
    else:
        cp = score.white().score(mate_score=100000)
        result["eval"] = f"{cp} cp"

    return result


# ---- SAVE RESULTS ----
def save_results_csv(results, system_prompt_path, model, tmp):
    results_dir = "tst_weird_puzzle_gpt"
    os.makedirs(results_dir, exist_ok=True)

    system_name = os.path.splitext(os.path.basename(system_prompt_path))[0]
    filename = os.path.join(results_dir, f"res_{system_name}_{model.replace('/', '-')}_T{tmp}.csv")

    norm_values = []
    legal_norms = []
    illegal_count = 0
    total_count = 0

    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["Call#", "Move", "Legal", "UCI", "Eval", "Normalized", "FEN"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for idx, res in enumerate(results, start=1):
            move_val = res['move']
            if len(move_val) > 10:
                move_val = "SE"
            
            norm_val = normalize_stockfish_0_1(res.get('eval', ''))
            
            writer.writerow({
                "Call#": idx,
                "Move": move_val,
                "Legal": res['legal'],
                "UCI": res.get('uci', ''),
                "Eval": res.get('eval', ''),
                "Normalized": round(norm_val, 3),
                "FEN": res.get("fen", "")
            })
            
            norm_values.append(norm_val)
            total_count += 1
            if res['legal']:
                legal_norms.append(norm_val)
            else:
                illegal_count += 1

        # Stats
        mean_val = statistics.mean(norm_values) if norm_values else 0.0
        std_val = statistics.pstdev(norm_values) if len(norm_values) > 1 else 0.0
        mae_val = statistics.mean(abs(v - 0.5) for v in norm_values) if norm_values else 0.0
        illegal_pct = (illegal_count / total_count * 100) if total_count > 0 else 0.0
        legal_mean = statistics.mean(legal_norms) if legal_norms else 0.0

        writer.writerow({})
        writer.writerow({"Move": "=== Summary Statistics ==="})
        writer.writerow({"Move": "Average Normalized Value", "Eval": round(mean_val, 3)})
        writer.writerow({"Move": "Standard Deviation", "Eval": round(std_val, 3)})
        writer.writerow({"Move": "Mean Absolute Error (from 0.5)", "Eval": round(mae_val, 3)})
        writer.writerow({"Move": "Illegal Moves (%)", "Eval": f"{illegal_pct:.2f}%"})
        writer.writerow({"Move": "Mean Value (Legal Moves Only)", "Eval": round(legal_mean, 3)})

    print(f"\n✅ Results saved to {filename}")


# ---- MAIN ----
class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    END = '\033[0m'

if __name__ == "__main__":
    models = [
        # "qwen/qwen-2.5-vl-7b-instruct",
        "openai/gpt-4.1-nano",
        # "amazon/nova-lite-v1",
        # "arcee-ai/afm-4.5b",
        # "baidu/ernie-4.5-21b-a3b",
        # "z-ai/glm-4-32b",
        # "bytedance/ui-tars-1.5-7b",
        # "google/gemini-2.5-flash-lite",
        # "mistralai/devstral-small",
        # "microsoft/phi-4-reasoning-plus",
    ]
    temper = [round(x * 0.1, 1) for x in range(11)]
    system_prompt_file = "./system_prompts/base.txt"
    fen_file = "391k-valid.fen"
    
    num_calls = 100
    fens = load_fens(fen_file)

    for tmp in temper:
        # pick ONE FEN for this temperature
        # idx = random.randint(0, len(fens)-1)
        # fen = fens[idx]
        # if len(fen.split()) == 4:
        #     fen = fen + " w - - 0 1"
        fen = "8/5pQB/6n1/6k1/6P1/6K1/8/8"
        fen = fen + " w - - 0 1"

        print(f"\n=== Temperature {Color.RED}{tmp}{Color.END} | Using FEN #{fen} ===")
        print(fen)

        # build prompt once
        query_prompt = build_prompt_from_fen(fen)

        for model in models:
            results = []
            print(f"\nTesting {Color.RED}{model}{Color.END} at temperature {Color.RED}{tmp}{Color.END}")

            for call_num in range(num_calls):
                board = chess.Board(fen)
                response = call_model(system_prompt_file, model, query_prompt, tmp)

                move_response = response.split("\n")[0].strip()
                move_result = parse_and_evaluate(move_response, board)
                move_result["fen"] = fen
                results.append(move_result)
                
                print(f"  Call {call_num+1}: Move={move_result['move']} | Legal={move_result['legal']} | Eval={move_result['eval']}")
                time.sleep(1)
            
            # Save per-model + per-temperature
            save_results_csv(results, system_prompt_file, model, tmp)

    engine.quit()

