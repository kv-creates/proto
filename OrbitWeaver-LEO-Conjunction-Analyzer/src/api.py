from fastapi import FastAPI
from .core import conjunction_report
app=FastAPI(title="OrbitWeaver")
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/conjunction")
def c(body: dict): return conjunction_report(body.get("tle1",{}), body.get("tle2",{}), body.get("times",[0,60,120]))
@app.get("/visual-data")
def v(): return {"orbits":conjunction_report({"a":7000,"inc":53},{"a":7010,"inc":53}, list(range(0,600,60)))}