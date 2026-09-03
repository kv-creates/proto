from fastapi import FastAPI
from .grammar import check
app=FastAPI()
@app.get("/health")
def h(): return {"status":"ok"}
