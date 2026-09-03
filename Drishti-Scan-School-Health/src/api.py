from fastapi import FastAPI
from .screen import vision_score
app=FastAPI()
@app.get("/health")
def h(): return {"status":"ok"}
