from ctransformers import AutoModelForCausalLM

llm = AutoModelForCausalLM.from_pretrained(
    "TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
    model_file="mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    model_type="mistral"
)

def generate_response(query, context=""):
    prompt = f"[INST] {context}\n{query} [/INST]"
    return llm(prompt)
