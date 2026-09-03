from fastapi import FastAPI
from .rti import draft_rti
app=FastAPI(title="NyayMitra")
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/draft")
def d(body: dict): return draft_rti(body.get("query",""))
