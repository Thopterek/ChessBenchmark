import chess
import chess.engine
from collections import defaultdict
import os
import time
import requests
import re
import csv
import statistics
import plotly.express as px

OP_TOKEN = os.environ.get("OP_TOKEN")

# ---- STOCKFISH SETUP ----
STOCKFISH_PATH = "/Users/salvador.dali.disciple/homebrew/bin/stockfish"
engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)


# ---- MODEL CALL FUNCTION ----
def call_model(system_prompt: str, model_name: str, quest: str, temp: float):
    try:
        with open(system_prompt, 'r', encoding='utf-8') as file:
            sys_prompt = file.read().strip()
    except FileNotFoundError:
        return "Error: System prompt file not found"
    
    try:
        with open(quest, 'r', encoding='utf-8') as file:
            quest_prompt = file.read().strip()
    except FileNotFoundError:
        return "Error: Quest prompt file not found"
    
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
                    {"role": "user", "content": quest_prompt}
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


def normalize_stockfish_0_1(eval_str, max_cp=1000):
    if not eval_str:
        return 0.0
    
    eval_str = eval_str.strip()
    
    mate_match = re.match(r"Mate in (-?\d+)", eval_str)
    if mate_match:
        mate_in = int(mate_match.group(1))
        if mate_in > 0:
            return max(0.0, min(1.0, 1 - 0.01 * (mate_in - 1)))
        else:
            return 0.0
    
    cp_match = re.match(r"(-?\d+)\s*cp", eval_str)
    if cp_match:
        cp = int(cp_match.group(1))
        cp = max(-max_cp, min(cp, max_cp))
        return 0.5 + (cp / (2 * max_cp))
    
    return 0.0


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


# ---- CSV RESULTS FUNCTION ----
def save_results_csv(results_list, system_prompt_path, query_prompt_path, model_name, tmp):
    results_dir = "tst"
    os.makedirs(results_dir, exist_ok=True)

    system_name = os.path.splitext(os.path.basename(system_prompt_path))[0]
    query_name = os.path.splitext(os.path.basename(query_prompt_path))[0]

    safe_model = model_name.replace("/", "_")
    base_filename = os.path.join(results_dir, f"res_{system_name}_{query_name}_{safe_model}_temp{tmp}.csv")

    norm_values = []
    legal_norms = []
    illegal_count = 0
    total_count = 0

    with open(base_filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["Call#", "Move", "Legal", "UCI", "Eval", "Normalized"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for idx, res in enumerate(results_list, start=1):
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
                "Normalized": round(norm_val, 3)
            })
            
            norm_values.append(norm_val)
            total_count += 1
            if res['legal']:
                legal_norms.append(norm_val)
            else:
                illegal_count += 1

        mean_val = statistics.mean(norm_values) if norm_values else 0.0
        std_val = statistics.pstdev(norm_values) if len(norm_values) > 1 else 0.0
        mae_val = statistics.mean(abs(v - 0.5) for v in norm_values) if norm_values else 0.0
        illegal_pct = (illegal_count / total_count * 100) if total_count > 0 else 0.0
        legal_mean = statistics.mean(legal_norms) if legal_norms else 0.0

        writer.writerow({})
        writer.writerow({"Call#": "=== Summary Statistics ==="})
        writer.writerow({"Call#": "Average Normalized Value", "Eval": round(mean_val, 3)})
        writer.writerow({"Call#": "Standard Deviation", "Eval": round(std_val, 3)})
        writer.writerow({"Call#": "Mean Absolute Error (from 0.5)", "Eval": round(mae_val, 3)})
        writer.writerow({"Call#": "Illegal Moves (%)", "Eval": f"{illegal_pct:.2f}%"})
        writer.writerow({"Call#": "Mean Value (Legal Moves Only)", "Eval": round(legal_mean, 3)})

    print(f"✅ Results saved to {base_filename}")


# ---- COLORS ----
class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    END = '\033[0m'


# ---- MAIN LOOP ----
if __name__ == "__main__":
    models = [
        "qwen/qwen-2.5-vl-7b-instruct",
        "openai/gpt-4.1-nano",
        "amazon/nova-lite-v1",
        "arcee-ai/afm-4.5b",
        "baidu/ernie-4.5-21b-a3b",
        "z-ai/glm-4-32b",
        "bytedance/ui-tars-1.5-7b",
        "google/gemini-2.5-flash-lite",
        "mistralai/devstral-small",
        "microsoft/phi-4-reasoning-plus",
    ]
    temper = [round(x * 0.1, 1) for x in range(11)]
    system_prompt_file = "./system_prompts/base.txt"
    query_prompt_file = "./user_prompt/week01Best.txt"
    
    num_calls = 1
    fen_str = "3qr2k/pbpp2pp/1p5N/3Q4/2P1P1b1/P7/1PP2PPP/R3RK2 w - - 0 1"

    for tmp in temper:
        for model in models:
            results = []
            print(f"\nTesting {Color.RED}{model}{Color.END} at temperature {Color.RED}{tmp}{Color.END}")
            
            for call_num in range(num_calls):
                print(f" Call #{Color.GREEN}{call_num+1}/{num_calls}{Color.END}")
                board = chess.Board(fen_str)
                response = call_model(system_prompt_file, model, query_prompt_file, tmp)
                
                move_response = response.split("\n")[0].strip()
                move_result = parse_and_evaluate(move_response, board)
                results.append(move_result)
                
                print(f"  Move: {move_result['move']} | Legal: {move_result['legal']} | Eval: {move_result['eval']}")
                time.sleep(1)
            
            # Save one CSV per model+temperature
            save_results_csv(results, system_prompt_file, query_prompt_file, model, tmp)

    engine.quit()
