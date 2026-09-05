from fastapi import FastAPI
from .core import aerocapture
app=FastAPI(title="AeroBrake")
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/capture")
def c(body: dict): return aerocapture(body.get("v_inf",10), body.get("peri",140))
@app.get("/visual-data")
def v(): return aerocapture(11,135)