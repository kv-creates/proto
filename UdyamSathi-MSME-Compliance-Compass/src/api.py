from fastapi import FastAPI
from .compliance import due_dates, penalty
app=FastAPI()
@app.get("/health")
def h(): return {"status":"ok"}
