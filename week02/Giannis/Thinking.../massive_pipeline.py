import chess
import chess.engine
from collections import defaultdict
import os
import time
import requests
import re
import csv
import statistics

OP_TOKEN = os.environ.get("OP_TOKEN")

# ---- STOCKFISH SETUP ----
STOCKFISH_PATH = "/Users/jtsiros93/homebrew/bin/stockfish"
engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

# ---- MODEL CALL FUNCTION WITH TOKEN COUNT ----
def call_model(system_prompt: str, model_name: str, quest: str, temp: float):
    try:
        with open(system_prompt, 'r', encoding='utf-8') as file:
            sys_prompt = file.read().strip()
    except FileNotFoundError:
        print("System prompt file not found")
        return {"content": "Error: System prompt file not found", "tokens": 0}
    
    try:
        with open(quest, 'r', encoding='utf-8') as file:
            quest_prompt = file.read().strip()
    except FileNotFoundError:
        print("Quest prompt file not found")
        return {"content": "Error: Quest prompt file not found", "tokens": 0}
    
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
                "temperature": temp
            }
        )
        
        if response.status_code == 200:
            result = response.json()
            content = result['choices'][0]['message']['content'].strip()
            tokens = result.get('usage', {}).get('total_tokens', 0)
            return {"content": content, "tokens": tokens}
        else:
            return {"content": f"Error: {response.status_code} - {response.text}", "tokens": 0}
            
    except Exception as e:
        return {"content": f"Error: {str(e)}", "tokens": 0}

# ---- HELPER FUNCTIONS ----
def normalize_stockfish_0_1(eval_str, max_cp=1000, min_cp=-1000):
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
        if cp >= 0:
            return 0.5 + 0.5 * min(cp, max_cp) / max_cp
        else:
            return 0.5 * max(cp, min_cp) / min_cp
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
    result = {"move": move_str, "uci": None, "legal": False, "eval": None, "fen": board.fen(), "tokens": 0}
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

# ---- SAVE CSV WITH METADATA, TOKENS, STDDEV ----
def save_results_csv(results_dict, task_info, output_dir="results"):
    os.makedirs(output_dir, exist_ok=True)
    system_name = os.path.splitext(os.path.basename(task_info['system_prompt']))[0]
    query_name = os.path.splitext(os.path.basename(task_info['prompt']))[0]
    
    base_filename = f"res_{system_name}_{query_name}.csv"
    filename = os.path.join(output_dir, base_filename)
    
    counter = 1
    while os.path.exists(filename):
        filename = os.path.join(output_dir, f"res_{system_name}_{query_name}_{counter}.csv")
        counter += 1
    
    total_norm = 0.0
    total_tokens = 0
    illegal_moves = 0
    count = 0
    norm_values = []

    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            "Model", "Call#", "Move", "Legal", "UCI", "Eval", "Normalized",
            "Tokens", "System Prompt", "Prompt", "FEN", "Temperature", "Number Calls"
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for model, responses in results_dict.items():
            for idx, res in enumerate(responses, start=1):
                move_val = res['move']
                if len(move_val) > 10:
                    move_val = "SE"
                norm_val = normalize_stockfish_0_1(res.get('eval', ''))
                norm_values.append(norm_val)
                writer.writerow({
                    "Model": model,
                    "Call#": idx,
                    "Move": move_val,
                    "Legal": res['legal'],
                    "UCI": res.get('uci', ''),
                    "Eval": res.get('eval', ''),
                    "Normalized": round(norm_val, 3),
                    "Tokens": res.get('tokens', 0),
                    "System Prompt": task_info['system_prompt'],
                    "Prompt": task_info['prompt'],
                    "FEN": task_info['fen_str'],
                    "Temperature": task_info['temperature'],
                    "Number Calls": task_info['number_calls']
                })
                total_norm += norm_val
                total_tokens += res.get('tokens', 0)
                if not res['legal']:
                    illegal_moves += 1
                count += 1

    average_norm = total_norm / count if count > 0 else 0
    stddev_norm = statistics.stdev(norm_values) if len(norm_values) > 1 else 0.0

    print(f"\nResults saved to {filename}")
    print(f"Average Normalized Value: {average_norm:.3f}")
    print(f"Standard Deviation of Normalized: {stddev_norm:.3f}")
    print(f"Total Tokens Used: {total_tokens}")
    print(f"Illegal Moves: {illegal_moves}")

    return average_norm, stddev_norm, total_tokens, illegal_moves

# ---- MAIN LOOP USING CSV ----
if __name__ == "__main__":
    tasks_csv = "tasks.csv"  # CSV columns: system_prompt,prompt,fen_str,number_calls,temperature,model
    summary_file = "summary_results.csv"
    summary_exists = os.path.exists(summary_file)

    with open(tasks_csv, newline='', encoding='utf-8') as csvfile, \
         open(summary_file, mode='a', newline='', encoding='utf-8') as summary_csv:
        
        reader = csv.DictReader(csvfile)
        summary_fieldnames = ["System Prompt", "Prompt", "FEN", "Number Calls", "Temperature", "Model",
                              "Average Normalized", "StdDev Normalized", "Total Tokens", "Illegal Moves Count"]
        summary_writer = csv.DictWriter(summary_csv, fieldnames=summary_fieldnames)
        
        if not summary_exists:
            summary_writer.writeheader()
        
        for task in reader:
            print(f"\nRunning task: {task}")
            results = defaultdict(list)
            num_calls = int(task['number_calls'])
            board_fen = task['fen_str']
            temperature = float(task['temperature'])
            model = task['model']

            for call_num in range(num_calls):
                print(f" Call #{call_num+1}/{num_calls}")
                board = chess.Board(board_fen)
                response = call_model(
                    task['system_prompt'],
                    model,
                    task['prompt'],
                    temperature
                )
                move_response = response['content'].split("\n")[0].strip()
                move_result = parse_and_evaluate(move_response, board)
                move_result['tokens'] = response['tokens']
                results[model].append(move_result)
                print(f"  Move: {move_result['move']} | Legal: {move_result['legal']} | Eval: {move_result['eval']} | Tokens: {response['tokens']}")
                time.sleep(1)
            
            avg_norm, stddev_norm, total_tokens, illegal_count = save_results_csv(results, task)
            
            # Append task summary
            summary_writer.writerow({
                "System Prompt": task['system_prompt'],
                "Prompt": task['prompt'],
                "FEN": task['fen_str'],
                "Number Calls": task['number_calls'],
                "Temperature": task['temperature'],
                "Model": task['model'],
                "Average Normalized": round(avg_norm, 3),
                "StdDev Normalized": round(stddev_norm, 3),
                "Total Tokens": total_tokens,
                "Illegal Moves Count": illegal_count
            })
    
    engine.quit()
