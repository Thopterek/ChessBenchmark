import chess
import chess.engine
from collections import defaultdict
import os
import time
import requests
import re
import csv

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


def normalize_stockfish_0_1(eval_str, max_cp=1000, min_cp=-1000):
    """
    Normalize Stockfish eval string to [0, 1] scale.
    Priority: Mate > positive cp > negative cp > invalid
    """
    if not eval_str:
        return 0.0  # invalid move
    
    eval_str = eval_str.strip()
    
    # Check for mate
    mate_match = re.match(r"Mate in (-?\d+)", eval_str)
    if mate_match:
        mate_in = int(mate_match.group(1))
        if mate_in > 0:
            # Winning mate: decay slightly with longer mates
            return max(0.0, min(1.0, 1 - 0.01 * (mate_in - 1)))
        else:
            # Losing mate: treat as worst
            return 0.0
    
    # Check for centipawns
    cp_match = re.match(r"(-?\d+)\s*cp", eval_str)
    if cp_match:
        cp = int(cp_match.group(1))
        if cp >= 0:
            return 0.5 + 0.5 * min(cp, max_cp) / max_cp
        else:
            return 0.5 * max(cp, min_cp) / min_cp  # negative cp mapped to [0, 0.5)
    
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
    and print average normalized value at the end.
    """
    results_dir = "results"
    os.makedirs(results_dir, exist_ok=True)

    system_name = os.path.splitext(os.path.basename(system_prompt_path))[0]
    query_name = os.path.splitext(os.path.basename(query_prompt_path))[0]
    filename = os.path.join(results_dir, f"res_{system_name}_{query_name}_{tmp}.csv")
    
    total_norm = 0.0
    count = 0

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
                
                total_norm += norm_val
                count += 1

    average_norm = total_norm / count if count > 0 else 0
    print(f"\nResults saved to {filename}")
    print(f"Average Normalized Value: {average_norm:.3f}")

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
    
    results = defaultdict(list)
    num_calls = 100
    fen_str = "3qr2k/pbpp2pp/1p5N/3Q4/2P1P1b1/P7/1PP2PPP/R3RK2 w - - 0 1"
    for tmp in temper:
        for model in models:
            print(f"\nTesting {model}")
            
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
        
        # Save CSV
        save_results_csv(results, system_prompt_file, query_prompt_file, tmp)
    
    engine.quit()