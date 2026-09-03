from fastapi import FastAPI
from .scam import analyze_sms
app=FastAPI()
@app.get("/health")
def h(): return {"status":"ok"}
