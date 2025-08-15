
import argparse, json
from transformers import pipeline

MODEL = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
TEMPLATE = """You are a document analyst. Extract deviations and risks from the text.
Return STRICT JSON array of objects with keys:
item, expected, found, risk (low|medium|high), explanation

Baseline expectations (examples):
- Termination notice >= 30 days
- Governing law = Delaware
- PHI requires Business Associate Agreement (BAA)

Document text:
---
{doc}
---
JSON ONLY:"""

def main(text: str):
    generator = pipeline("text-generation", model=MODEL, torch_dtype="auto", device_map="auto")
    prompt = TEMPLATE.format(doc=text[:4000])
    out = generator(prompt, max_new_tokens=512, do_sample=False)[0]["generated_text"]
    start = out.find("[")
    end = out.rfind("]")
    payload = out[start:end+1] if (start != -1 and end != -1 and end > start) else "[]"
    try:
        data = json.loads(payload)
    except Exception:
        data = []
    print(json.dumps({"model": MODEL, "deviations": data}, indent=2))

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--text-file", type=str, default="samples/sample_text.txt")
    args = ap.parse_args()
    text = open(args.text_file).read()
    main(text)
