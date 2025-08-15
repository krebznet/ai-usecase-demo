from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any, Dict, Optional, List
from analyzer import analyze

app = FastAPI(title="AI Usecase Demo API")

class AnalyzeReq(BaseModel):
    text: str
    baseline_path: Optional[str] = "baseline.yaml"

class AnalyzeResp(BaseModel):
    result: Dict[str, Any]

@app.post("/analyze", response_model=AnalyzeResp)
def analyze_endpoint(req: AnalyzeReq):
    result = analyze(req.text, req.baseline_path)
    return {"result": result}

# Optional: local LLM rationale via Ollama (if installed)
class ExplainReq(BaseModel):
    text: str
    hints: Optional[List[str]] = None        # e.g., ["Termination >= 30 days", "Gov law = Delaware"]
    model: Optional[str] = "llama3"          # any local model you've pulled with Ollama

class ExplainResp(BaseModel):
    model: str
    deviations: List[Dict[str, Any]]

@app.post("/explain", response_model=ExplainResp)
def explain(req: ExplainReq):
    try:
        import ollama
    except Exception as e:
        raise RuntimeError("Ollama not installed. pip install ollama && brew install ollama && ollama run llama3 once") from e

    hints_text = ""
    if req.hints:
        hints_text = "\n".join(f"- {h}" for h in req.hints)

    template = f"""You are a document analyst. Extract deviations and risks from the text.
Return STRICT JSON array of objects with keys:
item, expected, found, risk (low|medium|high), explanation

Baseline expectations (examples):
{hints_text if hints_text else "- Termination notice >= 30 days\n- Governing law = Delaware\n- PHI requires Business Associate Agreement (BAA)"} 

Document text:
---
{{doc}}
---
JSON ONLY."""

    prompt = template.format(doc=req.text[:6000])
    resp = ollama.chat(
        model=req.model or "llama3",
        messages=[{"role":"user","content": prompt}],
        options={"temperature": 0.0}
    )
    content = resp["message"]["content"]
    start = content.find("[")
    end = content.rfind("]")
    payload = content[start:end+1] if (start != -1 and end != -1 and end > start) else "[]"
    import json as _json
    try:
        data = _json.loads(payload)
    except Exception:
        data = []
    return {"model": req.model or "llama3", "deviations": data}
