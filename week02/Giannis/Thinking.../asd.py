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

# ---- MODEL CALL FUNCTION ----
def call_model(system_prompt: str, model_name: str, quest: str, temp: float):
    try:
        with open(system_prompt, 'r', encoding='utf-8') as file:
            sys_prompt = file.read().strip()
    except FileNotFoundError:
        print("System prompt file not found")
        return "Error: System prompt file not found"
    
    try:
        with open(quest, 'r', encoding='utf-8') as file:
            quest_prompt = file.read().strip()
    except FileNotFoundError:
        print("Quest prompt file not found")
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
                # "top_p": 0.1
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
    """
    Normalize Stockfish eval string to [0, 1] scale.
    Mate scores are prioritized as winning (1) or losing (0).
    cp scores are mapped linearly:
        -max_cp → 0.0
        0 → 0.5
        +max_cp → 1.0
    """
    if not eval_str:
        return 0.0  # invalid move
    
    eval_str = eval_str.strip()
    
    # Check for mate
    mate_match = re.match(r"Mate in (-?\d+)", eval_str)
    if mate_match:
        mate_in = int(mate_match.group(1))
        if mate_in > 0:
            return max(0.0, min(1.0, 1 - 0.01 * (mate_in - 1)))  # winning mate
        else:
            return 0.0  # losing mate
    
    # Check for centipawns
    cp_match = re.match(r"(-?\d+)\s*cp", eval_str)
    if cp_match:
        cp = int(cp_match.group(1))
        cp = max(-max_cp, min(cp, max_cp))  # clamp to range
        return 0.5 + (cp / (2 * max_cp))    # -max_cp→0.0, 0→0.5, +max_cp→1.0
    
    # Invalid / unknown
    return 0.0


# ---- PARSING FUNCTION ----
def clean_move_str(move_str: str) -> str:
    """
    Clean up LLM response to extract just the move notation
    """
    move_str = move_str.strip()
    move_str = re.sub(r'<[^>]+>', '', move_str)
    move_str = move_str.replace("**", "").replace("*", "").replace("__", "").replace("_", "")
    move_str = re.sub(r"[+#]", "", move_str)
    move_str = re.sub(r"^\d+\.\s*", "", move_str)
    move_str = re.sub(r"\([^)]*\)", "", move_str)
    move_str = re.sub(r'^[^\w]*|[^\w]*$', '', move_str)
    return move_str

def parse_and_evaluate(move_str: str, board: chess.Board):
    """
    Parse the LLM move in SAN, check legality, and evaluate with Stockfish.
    """
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

# ---- CSV RESULTS FUNCTION ----
def save_results_csv(results_dict, system_prompt_path, query_prompt_path, tmp):
    """
    Save results to CSV, including normalized Stockfish eval,
    and append summary statistics at the bottom.
    """
    results_dir = "results"
    os.makedirs(results_dir, exist_ok=True)

    system_name = os.path.splitext(os.path.basename(system_prompt_path))[0]
    query_name = os.path.splitext(os.path.basename(query_prompt_path))[0]
    base_filename = os.path.join(results_dir, f"res_{system_name}_{query_name}_{tmp}.csv")
    filename = base_filename

    # Ensure unique filename if file exists
    file_counter = 1
    while os.path.exists(filename):
        filename = base_filename.replace(".csv", f"_{file_counter}.csv")
        file_counter += 1

    norm_values = []
    legal_norms = []
    illegal_count = 0
    total_count = 0

    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["Model", "Call#", "Move", "Legal", "UCI", "Eval", "Normalized"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for model, responses in results_dict.items():
            for idx, res in enumerate(responses, start=1):
                move_val = res['move']
                if len(move_val) > 10:
                    move_val = "SE"
                
                norm_val = normalize_stockfish_0_1(res.get('eval', ''))
                
                writer.writerow({
                    "Model": model,
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

        # ---- Stats ----
        mean_val = statistics.mean(norm_values) if norm_values else 0.0
        std_val = statistics.pstdev(norm_values) if len(norm_values) > 1 else 0.0
        mae_val = statistics.mean(abs(v - 0.5) for v in norm_values) if norm_values else 0.0
        illegal_pct = (illegal_count / total_count * 100) if total_count > 0 else 0.0
        legal_mean = statistics.mean(legal_norms) if legal_norms else 0.0

        # Append summary rows
        writer.writerow({})
        writer.writerow({"Model": "=== Summary Statistics ==="})
        writer.writerow({"Model": "Average Normalized Value", "Eval": round(mean_val, 3)})
        writer.writerow({"Model": "Standard Deviation", "Eval": round(std_val, 3)})
        writer.writerow({"Model": "Mean Absolute Error (from 0.5)", "Eval": round(mae_val, 3)})
        writer.writerow({"Model": "Illegal Moves (%)", "Eval": f"{illegal_pct:.2f}%"})
        writer.writerow({"Model": "Mean Value (Legal Moves Only)", "Eval": round(legal_mean, 3)})

    print(f"\nResults saved to {filename}")


import plotly.express as px

# ---- MAIN LOOP ----
if __name__ == "__main__":
    models = [
        "google/gemini-2.5-flash-lite"
    ]
    temper = [
       0.0,
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
    system_prompt_file = "../system_prompts/MdLike.txt"
    query_prompt_file = "../prompts/week01Best.txt"
    
    num_calls = 100
    fen_str = "3qr2k/pbpp2pp/1p5N/3Q4/2P1P1b1/P7/1PP2PPP/R3RK2 w - - 0 1"

    temp_values = []
    avg_norm_values = []

    for tmp in temper:
        results = defaultdict(list)   # RESET per temperature run

        for model in models:
            print(f"\nTesting {model} at temperature {tmp}")
            
            for call_num in range(num_calls):
                print(f" Call #{call_num+1}/{num_calls}")
                board = chess.Board(fen_str)
                response = call_model(
                    system_prompt_file,
                    model,
                    query_prompt_file,
                    tmp
                )
                
                move_response = response.split("\n")[0].strip()
                move_result = parse_and_evaluate(move_response, board)
                results[model].append(move_result)
                
                print(f"  Move: {move_result['move']} | Legal: {move_result['legal']} | Eval: {move_result['eval']}")
                time.sleep(1)
        
        # Save CSV for this temperature
        save_results_csv(results, system_prompt_file, query_prompt_file, tmp)

        # --- Compute average normalized value for scatter plot ---
        norm_vals = [normalize_stockfish_0_1(r.get('eval', '')) for res in results.values() for r in res]
        avg_val = sum(norm_vals) / len(norm_vals) if norm_vals else 0.0
        temp_values.append(tmp)
        avg_norm_values.append(avg_val)

    engine.quit()

    # ---- PLOT SCATTER GRAPH ----
    fig = px.scatter(
        x=temp_values,
        y=avg_norm_values,
        labels={"x": "Temperature", "y": "Average Normalized Value"},
        title="Temperature vs Average Normalized Value"
    )
    fig.update_traces(mode="markers")  # scatter with connecting line
    fig.show()