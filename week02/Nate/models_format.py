import requests
from collections import defaultdict
import time
import os
import pandas as pd
import torch
import requests
from transformers import AutoTokenizer, AutoModel, AutoModelForCausalLM, pipeline

OP_TOKEN = os.environ.get("OP_TOKEN")

# Your existing function
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
                "max_tokens": 2000,
                "temperature": temp,
                "top_p": 0.1
            }
        )
        
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content'].strip()
        else:
            return f"Error: {response.status_code} - {response.text}"
            
    except Exception as e:
        return f"Error: {str(e)}"

# New function to format results as a table
def format_results_table(results_dict):
    """
    Format the results as a markdown table
    
    Args:
        results_dict: Dictionary with model names as keys and lists of responses as values
    """
    # Get all model names
    models = list(results_dict.keys())
    
    # Find the maximum number of responses for any model
    max_responses = max(len(responses) for responses in results_dict.values())
    
    # Create the table header
    header = "| " + " | ".join(models) + " |"
    separator = "|" + "|".join(["-" * (len(model) + 2) for model in models]) + "|"
    
    # Create the table rows
    rows = []
    for i in range(max_responses):
        row_cells = []
        for model in models:
            if i < len(results_dict[model]):
                row_cells.append(results_dict[model][i])
            else:
                row_cells.append("")
        rows.append("| " + " | ".join(row_cells) + " |")
    
    # Combine everything
    table = [header, separator] + rows
    return "\n".join(table)

# Debug colors
class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

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
    
    # Dictionary to store results
    results = defaultdict(list)
    
    print(f"{Color.BLUE}\n------------------------{Color.END}")
    print(f"{Color.BLUE}Testing the models{Color.END}")
    print(f"{Color.BLUE}------------------------{Color.END}")
    
    # Number of times to call each model
    num_calls = 10
    
    for model in models:
        print(f"\n{Color.YELLOW}Testing {model}{Color.END}")
        print(f"{Color.YELLOW}{'=' * (len(model) + 8)}{Color.END}")
        
        for call_num in range(num_calls):
            print(f"{Color.GREEN}Call #{call_num + 1}/{num_calls}{Color.END}")
            
            response = call_model(
                "./system_prompt/prompt_02.txt",
                model,
                "./query_prompt/01quest.txt",
                0.3
            )
            
            # Clean up the response to get just the move
            move_response = response.split('\n')[0]  # Take first line only
            move_response = move_response.replace('**', '').replace('*', '')  # Remove markdown
            move_response = move_response.strip()
            
            results[model].append(move_response)
            
            print(f"Response: {Color.RED}{move_response}{Color.END}")
            
            # Add a small delay to avoid rate limiting
            time.sleep(1)
        
        print(f"{Color.GREEN}Completed {model}{Color.END}")
    
    # Format and display results as table
    print(f"\n{Color.BLUE}{'=' * 50}{Color.END}")
    print(f"{Color.BLUE}FINAL RESULTS TABLE:{Color.END}")
    print(f"{Color.BLUE}{'=' * 50}{Color.END}")
    
    table_output = format_results_table(results)
    print(table_output)
    
    # Also save to file
    with open("model_results.md", "w", encoding="utf-8") as f:
        f.write("# Chess Move Prediction Results\n\n")
        f.write(table_output)
    
    print(f"\n{Color.GREEN}Results also saved to 'model_results.md'{Color.END}")