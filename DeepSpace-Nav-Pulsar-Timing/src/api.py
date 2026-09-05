from fastapi import FastAPI
from .core import xnav_position
app=FastAPI(title="DeepSpace")
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/xnav")
def x(body: dict): return xnav_position(body.get("pulsars",[]))
@app.get("/visual-data")
def v(): return xnav_position([{"residual":0.0001},{"residual":-0.00005}])