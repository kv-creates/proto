from fastapi import FastAPI
from .safety import segment_score, route_safety, safest_path
app = FastAPI(title="SurakshaPath")
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/score")
def score(seg: dict):
    hour = seg.pop("hour", 22)
    return {"safety": segment_score(seg, hour)}
@app.post("/route-safety")
def rs(body: dict):
    return route_safety(body["segments"], body.get("hour",22))
@app.post("/safest")
def sp(body: dict):
    return safest_path(body["graph"], body["start"], body["end"], body.get("hour",22))
