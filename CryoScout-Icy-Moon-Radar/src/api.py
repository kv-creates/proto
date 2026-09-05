from fastapi import FastAPI
from .core import radar_profile
app=FastAPI(title="CryoScout")
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/radar")
def r(body: dict): return radar_profile(body.get("thickness",10), body.get("ocean",True))
@app.get("/visual-data")
def v(): return {"profiles":[radar_profile(t) for t in [5,10,15,20]]}