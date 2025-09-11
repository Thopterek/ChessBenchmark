import os
import pandas
import torch
from transformers import AutoTokenizer, AutoModel, pipeline

# Version using the tokens that were given to us
AL_TOKEN = os.environ.get("ALEPH_TOKEN")

# Play around using the hugging face models
HF_TOKEN = os.environ.get("HF_TOKEN")

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

if __name__ == "__main__":
    result = lb_embedding("prompt_00.txt") 
