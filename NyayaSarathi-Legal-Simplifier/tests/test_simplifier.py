from src.simplifier import analyze_document, score_clause, simplify_clause
def test_risk_detection():
    r = score_clause("non-refundable deposit forfeit after lock-in 11 months")
    assert r["score"] >= 0.85
def test_simplify():
    assert "from now on" in simplify_clause("hereinafter referred").lower()
def test_analyze_sort():
    doc = "Simple clause. Non-refundable forfeit penalty 15% per month. Another simple."
    res = analyze_document(doc)
    assert res["clauses"][0]["risk_score"] >= res["clauses"][-1]["risk_score"]
