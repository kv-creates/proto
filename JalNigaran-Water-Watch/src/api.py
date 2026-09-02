from fastapi import FastAPI
from .water import tds_status, leakage_detect, tanker_need
app=FastAPI(title="JalNigaran")
@app.get("/health")
def h(): return {"status":"ok"}
@app.get("/tds/{val}")
def tds(val: int): return {"tds":val, "status": tds_status(val)}
@app.post("/leak")
def leak(body: dict): return leakage_detect(body.get("readings",[]))
@app.post("/forecast")
def fc(body: dict): return tanker_need(body.get("history",[]), body.get("tank_capacity",5000), body.get("current",1200))
