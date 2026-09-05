from fastapi import FastAPI
from .core import optimize
app=FastAPI(title="StarWeave")
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/optimize")
def o(body: dict): return optimize(body.get("planes",6), body.get("sats",22))
@app.get("/visual-data")
def v(): return optimize(6,22)