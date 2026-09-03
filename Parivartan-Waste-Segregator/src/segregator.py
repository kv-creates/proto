def classify_mock(h):
    return {"type":"wet" if h.get("h",0)>35 else "dry"}
