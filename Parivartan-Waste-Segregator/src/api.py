from fastapi import FastAPI
from .segregator import classify_mock
app=FastAPI()
@app.get("/health")
def h(): return {"status":"ok"}
