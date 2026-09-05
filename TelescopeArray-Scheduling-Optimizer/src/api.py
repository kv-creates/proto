from fastapi import FastAPI
from .core import schedule
app=FastAPI(title="TelescopeArray")
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/schedule")
def s(body: dict): return schedule(body.get("requests",[]))
@app.get("/visual-data")
def v(): return schedule([{"id":"M31","priority":3,"duration":60,"sun":100},{"id":"M42","priority":5,"duration":30,"sun":90}])