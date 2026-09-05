from fastapi import FastAPI
from .core import detect
app=FastAPI(title="ExoHunter")
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/detect")
def d(body: dict): return detect(body.get("flux",[1,0.99,1]), body.get("time",[0,1,2]))
@app.get("/visual-data")
def v():
    import math
    time=[i*0.1 for i in range(100)]
    flux=[1-0.01 if 30<i<35 else 1 for i in range(100)]
    return {"time":time,"flux":flux,"period":3.5}