import os
import pandas as pd
import torch
import requests
from transformers import AutoTokenizer, AutoModel, AutoModelForCausalLM, pipeline

# Version using the tokens that were given to us
AL_TOKEN = os.environ.get("ALEPH_TOKEN")

# Play around using the hugging face models
HF_TOKEN = os.environ.get("HF_TOKEN")

# Using the Open Router for different models
OP_TOKEN = os.environ.get("OP_TOKEN")

# 

# Legal-BERT embedding model tests
tokenizer = AutoTokenizer.from_pretrained("nlpaueb/legal-bert-base-uncased")
model = AutoModel.from_pretrained("nlpaueb/legal-bert-base-uncased")

# Function to process the file and return the embeddings
def lb_embedding(prompt_file: str):
    try:
        with open(prompt_file, 'r', encoding='utf-8') as file:
            text = file.read().strip()
    except FileNotFoundError:
        print("File not found")
        return
    
    # Ways to replace Python lists:
    #   pt = PyTorch tensors
    #   tf = TensorFlow tensors
    #   np = NumPy arrays
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state
    print("\nLegal-BERT embedding output")
    print(f"Embedding shape: {embeddings.shape}")
    print(f"Sequence length: {embeddings.shape[1]}")
    print(f"Embedding dimensions: {embeddings.shape[2]}")
    avg_embbed = tokens_from_embedded(embeddings, text, tokenizer)
    return embeddings
    
# trying to get more information about embedding
def tokens_from_embedded(embeddings, text, tokenizer):
    print("--- Embedding Analysis ---")
    tokens = tokenizer.convert_ids_to_tokens(tokenizer(text)['input_ids'])
    print(f"First 10 tokens: {tokens [:10]}")
    avg_embedd = embeddings.mean(dim=1).squeeze()
    print(f"Average vector: {avg_embedd[:10].tolist()}")
    return avg_embedd

# Generic Function to call the model 
def call_model(system_prompt: str, model_name: str, quest: str):
    try:
        with open(system_prompt, 'r', encoding='utf-8') as file:
            sys_prompt = file.read().strip()
    except FileNotFoundError:
        print("File not found")
        return
    try:
        with open(quest, 'r', encoding='utf-8') as file:
            quest_prompt = file.read().strip()
    except FileNotFoundError:
        print("File not found")
        return
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
            "max_tokens": 20,
            "temperature": 0.3,
            "top_p": 0.1
        }
    )
    if response.status_code == 200:
        result = response.json()
        print("Response:", result['choices'][0]['message']['content'])
    else:
        print("Error:", response.text)
    return

# debug colors
class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    END = '\033[0m'

if __name__ == "__main__":
    #embedd_eu_decision = lb_embedding("./prompts/prompt_00.txt") 
    #embedd_fide_rules = lb_embedding("./prompts/prompt_01.txt")
    print("\n------------------------")
    print("Going to test the models")
    print("------------------------")
    # two models that as for now have a chance to at least get the answer
    models = ["google/gemini-2.5-flash-lite", "openai/gpt-4.1-mini",
              "anthropic/claude-sonnet-4", "openai/gpt-3.5-turbo-instruct",
              "deepseek/deepseek-chat-v3.1",
              "meta-llama/llama-3.3-8b-instruct:free",
              "openai/gpt-5-chat", "qwen/qwen3-coder", "meituan/longcat-flash-chat",
              "mistralai/mistral-medium-3.1",
              "baidu/ernie-4.5-vl-28b-a3b"] 
    #for num in range(0, 10, +1):
    for model in models:
        print(f"Calling model {Color.RED}{model}{Color.END}")
        call_model("./system_prompt/based_on_claude.txt", model, "./query_prompt/just_pawn/prompt_best.txt")
        print(f"{Color.GREEN}NEXT MODEL GOING TO THE PIPE{Color.END}")