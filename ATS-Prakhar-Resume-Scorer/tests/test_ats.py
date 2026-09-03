from src.ats import parse_ats
def test_s(): assert parse_ats("python")["score"]>50
