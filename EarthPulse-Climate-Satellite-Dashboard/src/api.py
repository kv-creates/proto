from fastapi import FastAPI
from .core import fuse
app=FastAPI(title="EarthPulse")
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/fuse")
def f(body: dict): return fuse(body.get("ecostress",[]), body.get("modis",[]), body.get("grace",[]))
@app.get("/visual-data")
def v(): return fuse([10,11,10,12,10],[20,21,20,20,25],[5,5,5,5,6])