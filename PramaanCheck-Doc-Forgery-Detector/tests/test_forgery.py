from src.forgery import ensemble
import pathlib
from PIL import Image
def test_genuine(tmp_path):
    p=tmp_path/"img.jpg"
    Image.new("RGB",(100,100),color=(200,200,200)).save(p,"JPEG")
    r=ensemble(str(p), ocr_text="Regular text", qr_data="valid123")
    assert "risk_score" in r
    assert r["verdict"] in ["likely_genuine","suspicious","likely_forged"]
