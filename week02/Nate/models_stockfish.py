import chess
import chess.engine
from collections import defaultdict
import os
import time
import requests
import re

OP_TOKEN = os.environ.get("OP_TOKEN")

# ---- STOCKFISH SETUP ----
STOCKFISH_PATH = "/Users/salvador.dali.disciple/homebrew/bin/stockfish"  # update if needed
engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

def call_model(system_prompt: str, model_name: str, quest: str, temp: float):
    try:
        with open(system_prompt, 'r', encoding='utf-8') as file:
            sys_prompt = file.read().strip()
    except FileNotFoundError:
        print("File not found")
        return "Error: System prompt file not found"
    
    try:
        with open(quest, 'r', encoding='utf-8') as file:
            quest_prompt = file.read().strip()
    except FileNotFoundError:
        print("File not found")
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
                "messages": [{
                    "role": "system",
                    "content": sys_prompt
                },
                {
                    "role": "user",
                    "content": quest_prompt
                }],
                "max_tokens": 50
                # "temperature": temp,
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

# ---- PARSING FUNCTION ----
# def clean_move_str(move_str: str) -> str:
#     move_str = move_str.strip()
#     move_str = move_str.replace("**", "").replace("*", "")
#     move_str = re.sub(r"[+#]", "", move_str)       # remove check/mate
#     move_str = re.sub(r"^\d+\.\s*", "", move_str)  # remove move numbers
#     return move_str

def clean_move_str(move_str: str) -> str:
    """
    Clean up LLM response to extract just the move notation
    """
    # Remove common markdown and formatting
    move_str = move_str.strip()
    
    # Remove XML/HTML tags like <answer>, </answer>, etc.
    move_str = re.sub(r'<[^>]+>', '', move_str)
    
    # Remove markdown formatting
    move_str = move_str.replace("**", "").replace("*", "").replace("__", "").replace("_", "")
    
    # Remove check/mate symbols
    move_str = re.sub(r"[+#]", "", move_str)
    
    # Remove move numbers (e.g., "1.", "2.", etc.)
    move_str = re.sub(r"^\d+\.\s*", "", move_str)
    
    # Remove parentheses and their content
    move_str = re.sub(r"\([^)]*\)", "", move_str)
    
    # Remove any leading/trailing punctuation or whitespace
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
        return result  # stop early, since move was illegal

    # Stockfish evaluation
    info = engine.analyse(board, chess.engine.Limit(depth=15))
    score = info["score"]

    if score.is_mate():
        result["eval"] = f"Mate in {score.white().mate()}"
    else:
        cp = score.white().score(mate_score=100000)
        result["eval"] = f"{cp} cp"

    return result

# ---- RESULTS FORMAT ----
def format_results_table(results_dict):
    """
    Format results into markdown with legal/illegal split.
    """
    models = list(results_dict.keys())
    header = "| Model | Call # | Move | Legal | UCI | Eval |"
    separator = "|-------|--------|------|-------|-----|------|"
    
    rows = []
    for model, responses in results_dict.items():
        for idx, res in enumerate(responses, start=1):
            if len(res['move']) > 10:
                res['move'] = "SE"
            rows.append(
                f"| {model} | {idx} | {res['move']} | {res['legal']} "
                f"| {res.get('uci','')} | {res.get('eval','')} |"
            )
    
    return "\n".join([header, separator] + rows)

# ---- MAIN LOOP ----
if __name__ == "__main__":
    models = [
        "google/gemini-2.5-flash-lite", 
        "openai/gpt-4.1-mini",
        "anthropic/claude-sonnet-4", 
        "openai/gpt-3.5-turbo-instruct",
        "deepseek/deepseek-chat-v3.1",
        "meta-llama/llama-3.3-8b-instruct:free",
        "openai/gpt-5-chat", 
        "qwen/qwen3-coder", 
        "meituan/longcat-flash-chat",
        "mistralai/mistral-medium-3.1",
        "baidu/ernie-4.5-vl-28b-a3b"
    ]
    
    results = defaultdict(list)
    num_calls = 10
    fen_str = "r1bk3r/1pp2ppp/pb1p1n2/n2P4/B3P1q1/2Q2N2/PB3PPP/RN3RK1 w - - 0 1"
    
    for model in models:
        print(f"\nTesting {model}")
        
        for call_num in range(num_calls):
            print(f" Call #{call_num+1}/{num_calls}")
            board = chess.Board(fen_str)  # reset board for each round
            response = call_model(
                "./system_prompt/boc_code.txt",
                model,
                "./query_prompt/02quest.txt",
                0.3
            )
            
            move_response = response.split("\n")[0].strip()
            move_result = parse_and_evaluate(move_response, board)
            results[model].append(move_result)
            
            print(f"  Move: {move_result['move']} | Legal: {move_result['legal']} | Eval: {move_result['eval']}")
            time.sleep(1)
    
    # Final results
    table_output = format_results_table(results)
    print("\nFINAL RESULTS:\n")
    print(table_output)
    
    with open("model_results.md", "w", encoding="utf-8") as f:
        f.write("# Chess Move Prediction Results with Legality & Stockfish Eval\n\n")
        f.write(table_output)
    
    engine.quit()
