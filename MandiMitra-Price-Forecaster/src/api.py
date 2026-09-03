from fastapi import FastAPI
from .forecast import forecast
app=FastAPI()
@app.get("/health")
def h(): return {"status":"ok"}
