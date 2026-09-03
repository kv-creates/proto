def analyze_sms(t):
    return {"verdict":"scam" if "kyc" in t else "safe"}
