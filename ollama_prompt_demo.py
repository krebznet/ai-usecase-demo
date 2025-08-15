import argparse, json, sys
try:
    import ollama
except Exception as e:
    print("ImportError: make sure you `pip install ollama` and `brew install ollama && ollama run llama3` once.", file=sys.stderr)
    raise

MODEL = "llama3"  # you can change to 'llama3.1' or any pulled model

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
JSON ONLY."""

def main(text: str):
    prompt = TEMPLATE.format(doc=text[:6000])
    resp = ollama.chat(
        model=MODEL,
        messages=[{"role":"user","content": prompt}],
        options={"temperature": 0.0}
    )
    content = resp["message"]["content"]
    start = content.find("[")
    end = content.rfind("]")
    payload = content[start:end+1] if (start != -1 and end != -1 and end > start) else "[]"
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
