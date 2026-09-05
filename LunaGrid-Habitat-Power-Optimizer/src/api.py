from fastapi import FastAPI
from .core import simulate
app=FastAPI(title="LunaGrid")
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/simulate")
def s(body: dict): return simulate(body.get("solar",[5]*24), body.get("load",[3]*24))
@app.get("/visual-data")
def v(): return simulate([8 if i%24>6 else 0 for i in range(48)], [3]*48)