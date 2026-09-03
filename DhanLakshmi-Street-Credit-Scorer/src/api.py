from fastapi import FastAPI
from .credit import credit_score
app=FastAPI()
@app.get("/health")
def h(): return {"status":"ok"}
