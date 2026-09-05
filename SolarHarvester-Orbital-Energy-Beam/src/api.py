from fastapi import FastAPI
from .core import beam_efficiency
app=FastAPI(title="SolarHarvester")
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/beam")
def b(body: dict): return beam_efficiency(body.get("array_kw",1000))
@app.get("/visual-data")
def v(): return beam_efficiency(2000)