from fastapi import FastAPI
from .core import detect_craters
app=FastAPI(title="AstroCartographer")
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/detect")
def d(body: dict): return detect_craters(body.get("image",[]))
@app.get("/visual-data")
def v(): return detect_craters([{"x":10,"y":20,"r":12,"contrast":0.8},{"x":30,"y":40,"r":4,"contrast":0.6}])