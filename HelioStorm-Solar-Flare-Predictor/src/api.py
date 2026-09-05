from fastapi import FastAPI
from .core import predict
app=FastAPI(title="HelioStorm")
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/predict")
def p(body: dict): return predict(body.get("series",[{"usflux":1000,"totpot":2000}]))
@app.get("/visual-data")
def v(): return {"flux":[1,2,5,9,4,2],"prob":0.65}