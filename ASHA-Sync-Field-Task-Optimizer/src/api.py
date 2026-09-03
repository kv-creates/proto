from fastapi import FastAPI
from .optimizer import optimize
app=FastAPI()
@app.get("/health")
def h(): return {"status":"ok"}
