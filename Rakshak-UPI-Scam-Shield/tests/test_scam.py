from src.scam import analyze_sms
def test_s(): assert analyze_sms("kyc blocked")["verdict"]=="scam"
