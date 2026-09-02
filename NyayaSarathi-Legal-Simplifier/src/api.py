from fastapi import FastAPI
from pydantic import BaseModel
from .simplifier import analyze_document

app = FastAPI(title="NyayaSarathi API", version="1.0.0")

class AnalyzeReq(BaseModel):
    text: str
    hindi: bool = False

@app.get("/health")
def health(): return {"status":"ok","service":"nyaya-sarathi"}

@app.post("/analyze")
def analyze(req: AnalyzeReq):
    return analyze_document(req.text, to_hindi=req.hindi)

@app.get("/")
def root(): return {"message":"NyayaSarathi - POST /analyze with {text, hindi}"}
