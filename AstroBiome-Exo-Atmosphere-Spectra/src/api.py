from fastapi import FastAPI
from .core import transmission
app=FastAPI(title="AstroBiome")
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/analyze")
def a(body: dict): return transmission(body.get("depths",{}))
@app.get("/visual-data")
def v(): return transmission({"1.4":0.002,"3.3":0.001,"4.3":0.0005})