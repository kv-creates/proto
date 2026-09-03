from fastapi import FastAPI
from .grievance import predict
app=FastAPI()
@app.get("/health")
def h(): return {"status":"ok"}
