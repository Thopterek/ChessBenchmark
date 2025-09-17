
import os
import torch
import requests
import pandas as pd
from transformers import AutoTokenizer, AutoModel

AL_TOKEN = os.environ.get("ALEPH_TOKEN")
HF_TOKEN = os.environ.get("HF_TOKEN")
OP_TOKEN = os.environ.get("OP_TOKEN")

# Legal-BERT embedding model tests
tokenizer = AutoTokenizer.from_pretrained("nlpaueb/legal-bert-base-uncased")
model = AutoModel.from_pretrained("nlpaueb/legal-bert-base-uncased")

def lb_embedding(prompt_file: str):
    try:
        with open(prompt_file, 'r', encoding='utf-8') as file:
            text = file.read().strip()
    except FileNotFoundError:
        print("File not found")
        return
    
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state
    avg_embbed = tokens_from_embedded(embeddings, text, tokenizer)
    return embeddings

def tokens_from_embedded(embeddings, text, tokenizer):
    tokens = tokenizer.convert_ids_to_tokens(tokenizer(text)['input_ids'])
    avg_embedd = embeddings.mean(dim=1).squeeze()
    return avg_embedd

def call_model(system_prompt: str, model_name: str, quest: str):
    try:
        with open(system_prompt, 'r', encoding='utf-8') as file:
            sys_prompt = file.read().strip()
    except FileNotFoundError:
        print("File not found")
        return None
    try:
        with open(quest, 'r', encoding='utf-8') as file:
            quest_prompt = file.read().strip()
    except FileNotFoundError:
        print("File not found")
        return None
    
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
            "max_tokens": 50
        }
    )
    
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content'].strip().replace("\n", " ")
    else:
        print("Error:", response.text)
        return "ERROR"

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    END = '\033[0m'

if __name__ == "__main__":
    print("\n------------------------")
    print("Going to test the models")
    print("------------------------")

    models = [
        "google/gemini-2.5-flash-lite",
        "openai/gpt-4.1-mini",
        "anthropic/claude-sonnet-4",
        "openai/gpt-3.5-turbo-instruct",
        "nvidia/nemotron-nano-9b-v2:free",
        "deepseek/deepseek-chat-v3.1:free",
        "meta-llama/llama-3.3-8b-instruct:free"
    ]

    # Collect results row
    row_data = []
    headers = [m.split("/")[-1].replace(":free", "") for m in models]

    for model in models:
        print(f"Calling model {Color.RED}{model}{Color.END}")
        response = call_model("./system_prompts/FEN_bare.txt", model, "./prompts/DoYouKnowFen.txt")
        row_data.append(response if response else "ERROR")
        print(f"{Color.GREEN}NEXT MODEL GOING TO THE PIPE{Color.END}")

    # Write markdown file
    md_file = "results.md"

    if not os.path.exists(md_file):
        # Write header and separator row first
        with open(md_file, "w", encoding="utf-8") as f:
            f.write("| " + " | ".join(headers) + " |\n")
            f.write("|" + " --- |" * len(headers) + "\n")

    # Append the new row
    with open(md_file, "a", encoding="utf-8") as f:
        f.write("| " + " | ".join(row_data) + " |\n")

    print(f"\nResults appended to {md_file}")
