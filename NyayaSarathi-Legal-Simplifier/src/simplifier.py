"""
NyayaSarathi - Legal clause simplifier & risk scorer
- Extracts clauses via sentence segmentation
- Scores risk using weighted lexicon (auto-renewal, penalty, lock-in, etc.)
- Simplifies to plain English/Hindi via rule-based paraphraser (LLM-ready hook)
"""
import re
from typing import List, Dict

RISK_LEXICON = {
    r"auto.?renew": (0.9, "Auto-renewal without notice"),
    r"non.?refundable": (0.85, "Non-refundable payment"),
    r"forfeit": (0.85, "Forfeiture clause"),
    r"penalty.*\d+%": (0.8, "High penalty percentage"),
    r"lock.?in.*\d+.*month": (0.75, "Long lock-in period"),
    r"sole discretion": (0.7, "One-sided discretion"),
    r"without.*notice": (0.7, "No-notice termination"),
    r"indemnify": (0.65, "Indemnity burden"),
    r"jurisdiction.*\b(Delhi|Mumbai)\b": (0.5, "Distant jurisdiction"),
    r"interest.*\d+%.*per month": (0.9, "Exorbitant monthly interest"),
}

PLAIN_MAP = {
    "hereinafter": "from now on",
    "notwithstanding": "even though",
    "hereto": "to this agreement",
    "whereas": "because",
    "aforementioned": "mentioned earlier",
    "indemnify": "compensate for loss",
    "sole discretion": "only our choice",
    "forfeit": "lose",
}

def split_clauses(text: str) -> List[str]:
    # naive clause splitter by numbered points or sentences
    parts = re.split(r'(?:\n\s*\d+[\.)]\s*|;\s*|\.\s+)', text.strip())
    return [p.strip() for p in parts if len(p.strip()) > 20]

def score_clause(clause: str) -> Dict:
    risks = []
    score = 0.0
    low = clause.lower()
    for pat, (w, label) in RISK_LEXICON.items():
        if re.search(pat, low):
            risks.append({"pattern": pat, "label": label, "weight": w})
            score = max(score, w)
    # boost if multiple risks
    if len(risks) >= 2:
        score = min(0.99, score + 0.1 * (len(risks)-1))
    return {"score": round(score, 2), "risks": risks}

def simplify_clause(clause: str) -> str:
    out = clause
    for k, v in PLAIN_MAP.items():
        out = re.sub(re.escape(k), v, out, flags=re.I)
    # shorten long sentences
    out = re.sub(r'\s+', ' ', out).strip()
    return out

def simplify_hindi_stub(clause: str) -> str:
    # stub: rule-based + prefix; plug LLM here
    return "[HI] " + simplify_clause(clause) + " (सरल हिंदी)"

def analyze_document(text: str, to_hindi=False) -> Dict:
    clauses = split_clauses(text)
    results = []
    overall = 0.0
    for c in clauses:
        s = score_clause(c)
        overall = max(overall, s["score"])
        simplified = simplify_hindi_stub(c) if to_hindi else simplify_clause(c)
        results.append({
            "original": c,
            "simplified": simplified,
            "risk_score": s["score"],
            "risks": s["risks"]
        })
    # sort by risk descending
    results.sort(key=lambda x: x["risk_score"], reverse=True)
    return {"overall_risk": overall, "clauses": results, "summary": f"Found {len([r for r in results if r['risk_score']>0.6])} high-risk clauses out of {len(results)} total."}

if __name__ == "__main__":
    sample = open("demo/sample_agreement.txt", encoding="utf-8").read() if os.path.exists("demo/sample_agreement.txt") else "The tenant shall forfeit deposit if lock-in 11 months broken. Non-refundable brokerage. Jurisdiction Delhi sole discretion."
    import os, json
    print(json.dumps(analyze_document(sample, to_hindi=False), indent=2, ensure_ascii=False))
