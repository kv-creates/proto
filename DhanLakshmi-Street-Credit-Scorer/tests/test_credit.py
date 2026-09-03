from src.credit import credit_score
def test_c(): assert credit_score([],[],[])["tier"] in ["A","B","C"]
