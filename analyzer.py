
import argparse, yaml, re, json
from typing import List, Dict, Any
from sentence_transformers import SentenceTransformer, util

EMB_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
_model = None

def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(EMB_MODEL_NAME)
    return _model

def chunk_text(text: str) -> List[str]:
    parts = re.split(r'(?<=[.;:])\s+', text)
    return [p.strip() for p in parts if p.strip()]

def load_baseline(path: str) -> Dict[str, Any]:
    with open(path, "r") as f:
        return yaml.safe_load(f)

def find_best_matches(chunks: List[str], baseline_texts: Dict[str, str]) -> Dict[str, Dict[str, Any]]:
    model = get_model()
    chunk_embs = model.encode(chunks, convert_to_tensor=True, normalize_embeddings=True)
    out = {}
    for key, text in baseline_texts.items():
        base_emb = model.encode([text], convert_to_tensor=True, normalize_embeddings=True)
        cos_scores = util.cos_sim(base_emb, chunk_embs)[0]
        best_idx = int(cos_scores.argmax())
        out[key] = {
            "best_chunk": chunks[best_idx],
            "score": float(cos_scores[best_idx]),
            "index": best_idx
        }
    return out

def apply_rules(baseline: Dict[str, Any], matches: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    deviations = []
    for key, meta in baseline["requirements"].items():
        m = matches.get(key, {})
        found = m.get("best_chunk", "")
        score = m.get("score", 0.0)
        rule_type = meta.get("type")
        if rule_type == "numeric_days":
            nums = [int(x) for x in re.findall(r'(\\d+)\\s*day', found.lower())]
            found_days = nums[0] if nums else None
            expected = meta.get("expected_min_days", 30)
            if found_days is None or found_days < expected:
                deviations.append({
                    "item": key,
                    "expected": f">= {expected} days",
                    "found": f"{found_days} days" if found_days is not None else "N/A",
                    "risk": meta.get("risk_if_below", "medium"),
                    "similarity": round(score, 3),
                    "evidence": found
                })
        elif rule_type == "keyword":
            expected_val = meta.get("expected_value", "").lower()
            if expected_val and expected_val not in found.lower():
                deviations.append({
                    "item": key,
                    "expected": expected_val,
                    "found": found[:300],
                    "risk": meta.get("risk_if_mismatch", "low"),
                    "similarity": round(score, 3),
                    "evidence": found
                })
        elif rule_type == "must_include_any":
            req = [kw.lower() for kw in meta.get("required_keywords", [])]
            if not any(kw in found.lower() for kw in req):
                deviations.append({
                    "item": key,
                    "expected": f"include one of: {', '.join(req)}",
                    "found": found[:300],
                    "risk": meta.get("risk_if_missing", "high"),
                    "similarity": round(score, 3),
                    "evidence": found
                })
        else:
            pass
    return deviations

def analyze(text: str, baseline_path: str = "baseline.yaml") -> Dict[str, Any]:
    baseline = load_baseline(baseline_path)
    chunks = chunk_text(text)
    baseline_texts = {k:v["text"] for k,v in baseline["requirements"].items()}
    matches = find_best_matches(chunks, baseline_texts)
    deviations = apply_rules(baseline, matches)
    return {"chunks": chunks, "matches": matches, "deviations": deviations}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--text-file", type=str, default="samples/sample_text.txt")
    ap.add_argument("--baseline", type=str, default="baseline.yaml")
    args = ap.parse_args()
    with open(args.text_file, "r") as f:
        text = f.read()
    result = analyze(text, args.baseline)
    print(json.dumps(result, indent=2))
