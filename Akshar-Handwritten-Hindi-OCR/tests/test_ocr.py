from src.ocr import pipeline
def test_o(): assert "नमस्ते" in pipeline("x")["ocr"]["text"]
