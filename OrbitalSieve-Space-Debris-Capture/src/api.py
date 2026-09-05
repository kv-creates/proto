from fastapi import FastAPI
from .core import plan
app=FastAPI(title="OrbitalSieve")
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/plan")
def p(body: dict): return plan(body.get("debris",{}))
@app.get("/visual-data")
def v(): return plan({"a":7500,"spin":2,"mass":200})