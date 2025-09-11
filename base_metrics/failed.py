# problems with how huge the model is, left out for now
def call_microsoft():
    micro_tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-4-reasoning")
    micro_model = AutoModelForCausalLM.from_pretrained("microsoft/Phi-4-reasoning", device_map="auto", torch_dtype="auto")

    messages = [
        {"role": "system", "content": """
        <Base> </Base>
        """
        },
        {"role": "user", "content": "What is the derivative of x^2?"},
    ]
    inputs = micro_tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt")

    outputs = micro_model.generate(
        inputs.to(model.device),
        max_new_tokens=256,
        temperature=0.8,
        top_k=50,
        top_p=0.95,
        do_sample=True,
    )
    print(micro_tokenizer.decode(outputs[0]))

# THE BOARD PRESENTED IN FEN
# 3qr2k/pbpp2pp/1p5N/3Q4/2P1P1b1/P7/1PP2PPP/R3RK2 w - - 0 1

# MODELS THAT FAIL AT ALL TIMES AND ARE DAMN COSTLY
# Calling model thedrummer/anubis-70b-v1.1
# Response: <answer>Nxg6+</answer>
"thedrummer/anubis-70b-v1.1"

# Too damn costly doesn't even listen to syntax rules:
"anthropic/claude-sonnet-4"

# Constantly failing at keeping the rules and syntax:
"openai/gpt-3.5-turbo-instruct"

# Might be the problem of the privacy settings to be retested
# Calling model qwen/qwen3-coder:free
# Error: {"error":{"message":"No endpoints found matching your data policy (Free model training). Configure: https://openrouter.ai/settings/privacy","code":404}}

# Calling model tencent/hunyuan-a13b-instruct:free
# Error: {"error":{"message":"No endpoints found matching your data policy (Free model training). Configure: https://openrouter.ai/settings/privacy","code":404}}

# Calling model moonshotai/kimi-dev-72b:free
# Error: {"error":{"message":"No endpoints found matching your data policy (Free model training). Configure: https://openrouter.ai/settings/privacy","code":404}}

# Calling model nvidia/llama-3.1-nemotron-ultra-253b-v1:free
# Error: {"error":{"message":"No endpoints found matching your data policy (Free model training). Configure: https://openrouter.ai/settings/privacy","code":404}}