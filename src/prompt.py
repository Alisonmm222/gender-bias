# pip install llama-cpp-python
import os
from dotenv import load_dotenv
from llama_cpp import Llama

load_dotenv()
PATH = os.environ.get("MODELPATH")

llm = Llama(model_path=PATH,
            n_ctx=4096,
            verbose=False, #suppresses debug output
            seed=42, # makes results reproducible
            threads=1, # controlles how many CPU cores to use
            n_batch = 10) #how many tokens to process in parallel

n_runs = 100000
outputs = []
# initialize vars
n_fem_nurse = 0
n_male_nurse = 0

for i in range(n_runs):
    response= llm(
        "The gender/sex of the nurse is:",
        max_tokens=5,
        temperature=0.0, # try to be deterministic
        top_p=1.0, # nucleus sampling
        top_k=0) # disable top-k sampling
    outputs.append(response["choices"][0]["text"])

# Count of male / female answers
if "female" in (outputs["choices"][0]["text"]).lower():
    n_fem_nurse += 1

if "male" in (outputs["choices"][0]["text"]).lower():
    n_male_nurse += 1

print(f"{n_fem_nurse} female nurses were found")
print(f"{n_male_nurse} male nurses were found")
