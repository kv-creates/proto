from fastapi import FastAPI
from .ats import parse_ats
app=FastAPI()
@app.get("/health")
def h(): return {"status":"ok"}
