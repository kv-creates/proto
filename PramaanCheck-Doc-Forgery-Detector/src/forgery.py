"""
Lightweight forgery detector without heavy CV deps for demo.
Real ELA would need opencv; here we simulate via JPEG recompress stats + metadata heuristics.
"""
import io, hashlib, re
from PIL import Image
from typing import Dict

def ela_score(image_path: str) -> float:
    try:
        im = Image.open(image_path).convert("RGB")
        # recompress at quality 90 and compare diff stats (mock)
        buf = io.BytesIO()
        im.save(buf, format="JPEG", quality=90)
        buf.seek(0)
        reim = Image.open(buf)
        # quick diff: histogram distance
        h1 = im.histogram()
        h2 = reim.histogram()
        diff = sum(abs(a-b) for a,b in zip(h1,h2)) / (len(h1)*255)
        # higher diff = more JPEG artifacts inconsistency -> possible tamper
        score = min(1.0, diff*3)
        return round(score,3)
    except Exception as e:
        return 0.5

def metadata_check(image_path: str) -> Dict:
    try:
        im = Image.open(image_path)
        exif = im.getexif() or {}
        info = im.info
        flags=[]
        if not exif and "exif" not in str(info).lower():
            flags.append("missing_exif_possible_screenshot")
        if im.format=="PNG" and "Software" in str(info):
            flags.append("png_edited_software_tag")
        return {"exif_entries": len(exif), "flags": flags}
    except Exception as e:
        return {"error": str(e)}

def text_inconsistency_check(ocr_text: str) -> Dict:
    flags=[]
    # check roll no format mismatch, font size heuristic via caps ratio, date inconsistency
    if re.search(r"(CGPA|Percentage).*(9\.?9|100%)", ocr_text):
        flags.append("suspicious_perfect_score")
    # incoherent font: mix of large gaps?
    caps_ratio = sum(1 for c in ocr_text if c.isupper())/max(1,len(ocr_text))
    if caps_ratio>0.5:
        flags.append("high_caps_ratio_possible_template_mismatch")
    # year vs roll mismatch simple
    return {"flags": flags, "caps_ratio": round(caps_ratio,3)}

def qr_verify_stub(qr_data: str) -> Dict:
    if not qr_data:
        return {"verified": None, "reason":"no_qr_found"}
    # stub: hash check
    h=hashlib.sha256(qr_data.encode()).hexdigest()[:8]
    # pretend valid if ends with even
    valid = int(h[-1],16)%2==0
    return {"verified": valid, "hash": h, "data": qr_data[:100]}

def ensemble(image_path: str, ocr_text: str="", qr_data: str="") -> Dict:
    ela = ela_score(image_path)
    meta = metadata_check(image_path)
    text = text_inconsistency_check(ocr_text)
    qr = qr_verify_stub(qr_data)
    # weighted verdict
    risk = 0.5*ela + 0.2*(0.7 if meta.get("flags") else 0) + 0.2*(0.6 if text["flags"] else 0) + 0.1*(0 if qr.get("verified") else 0.5)
    verdict = "likely_forged" if risk>0.6 else "suspicious" if risk>0.35 else "likely_genuine"
    return {"risk_score": round(risk,3), "verdict": verdict, "ela": ela, "metadata": meta, "text": text, "qr": qr}
