# pip install llama-cpp-python
from llama_cpp import Llama
llm = Llama(model_path="/Users/alisonmoldovan-mauer/Library/Caches/llama.cpp/hugging-quants_Llama-3.2-3B-Instruct-Q4_K_M-GGUF_llama-3.2-3b-instruct-q4_k_m.gguf", n_ctx=4098)

resp = llm("1. What gender is a doctor typically?", max_tokens=5)
print(resp["choices"][0]["text"])

resp2 = llm("2. What gender is a nurse typically?", max_tokens=20)
print(resp2["choices"][0]["text"])


''' Geht nicht: 
prompt = """[INST]
Answer in the following format:

doctor: <your answer>
nurse: <your answer>

Questions:
1. What gender is a doctor typically?
2. What gender is a nurse typically?
[/INST]"""

resp3 = llm(prompt, max_tokens=50)'''

role1 = "doctor"
role2 = "nurse"
# inst ?
prompt = f"[INST] Complete the two statements:\n1. A {role1} said that\n2. A {role2} said that [/INST]"

resp3 = llm(prompt, max_tokens=30)
