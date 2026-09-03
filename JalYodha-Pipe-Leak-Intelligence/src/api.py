from fastapi import FastAPI
from .leak import night_flow_leak
app=FastAPI()
@app.get("/health")
def h(): return {"status":"ok"}
