from fastapi import FastAPI
from .pest import classify, outbreak_score
app=FastAPI(title="KrishiDhwani")
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/classify")
def c(body: dict): return classify(body)
@app.post("/outbreak")
def o(body: dict): return outbreak_score(body.get("reports",[]))
