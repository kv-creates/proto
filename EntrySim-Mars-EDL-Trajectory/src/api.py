from fastapi import FastAPI
from .core import edl_sim
app=FastAPI(title="EntrySim")
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/simulate")
def s(body: dict): return edl_sim(body.get("v",5800), body.get("angle",-12))
@app.get("/visual-data")
def v(): return edl_sim()