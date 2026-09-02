from fastapi import FastAPI, UploadFile, File
from .forgery import ensemble
import tempfile, shutil
app = FastAPI(title="PramaanCheck")
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/verify")
def verify(file: UploadFile = File(...), ocr_text: str = "", qr_data: str = ""):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        shutil.copyfileobj(file.file, tmp)
        path=tmp.name
    return ensemble(path, ocr_text, qr_data)
