from llama_cpp import Llama
import os
from dotenv import load_dotenv

load_dotenv()
PATH = os.environ.get("MODELPATH")

def rng_checks():
    llm_rngcheck = Llama(model_path=PATH, do_sample = True,temperature=0.0,top_p=1.0,top_k=0,seed=42,n_ctx=256, max_tokens=50,
        n_gpu_layers=-1, verbose=False, threads=7, n_batch=256)
    
    # Prompts
    prompt = "Tell me a joke."
    n_runs = 1
    run_id = 0

    for i in range(n_runs):
        output = llm_rngcheck(prompt)
        raw_text = output["choices"][0]["text"].strip() # store raw text
        print({
            "run_id": run_id,
            "prompt": prompt,
            "raw_output": raw_text,
        })
        run_id += 1

if __name__ == "__main__":
    rng_checks()

    