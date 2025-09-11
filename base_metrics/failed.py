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