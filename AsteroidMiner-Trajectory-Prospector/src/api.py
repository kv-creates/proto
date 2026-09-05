from fastapi import FastAPI
from .core import porkchop
app=FastAPI(title="AsteroidMiner")
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/porkchop")
def p(body: dict): return porkchop(body.get("r1",1.5), body.get("r2",2.2), body.get("tofs",[100,200,300]))
@app.get("/visual-data")
def v(): return porkchop(1,1.5,[80,120,200])