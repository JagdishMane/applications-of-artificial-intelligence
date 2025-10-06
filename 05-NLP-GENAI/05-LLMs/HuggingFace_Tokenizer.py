from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "meta-llama/Meta-LIama-3-70B-Instruct"

## Load Tokenizer and model
### Causal Language Model - Predicts next token in sequence
tokenizer = AutoTokenizer.from_pretrained(model_id)             ### Text to token 
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")  ### next token prediction


# Input text
text = "What is the capital of India ?"
#Toeknize and generate
inputs = tokenizer(text, return_tensors="pt").to(model.device)  ### Token to text ids
outputs = model.generate(**inputs, max_new_tokens=50)          ### Generate next tokens

# Decode the output tokens to text
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(generated_text)
### Summarization


## Chat Model - Predicts next token in sequence based on chat history
# model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"

# tokenizer = AutoTokenizer.from_pretrained(model_id)             ### Text to token
# model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")  ### next token prediction
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of India ?"},
    {"role": "assistant", "content": "The capital of India is New Delhi."},
    {"role": "user", "content": "What is the capital of USA ?"}
]

prompt = tokenizer.apply_chat_template(messages,tokenizer=False,add_gen_tokens=True)

print("Prompt: ", prompt)