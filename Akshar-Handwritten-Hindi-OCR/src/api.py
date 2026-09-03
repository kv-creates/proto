from fastapi import FastAPI
from .ocr import pipeline
app=FastAPI()
@app.get("/health")
def h(): return {"status":"ok"}
