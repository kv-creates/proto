from fastapi import FastAPI
from .core import plan
app=FastAPI(title="LunaTerra")
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/plan")
def p(body: dict): return plan(body.get("hab",{}))
@app.get("/visual-data")
def v(): return plan({"wall_h":3,"perim":40,"volume":12})