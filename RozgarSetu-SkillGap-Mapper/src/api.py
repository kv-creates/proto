from fastapi import FastAPI
from pydantic import BaseModel
from .skills import gap, learning_path
app=FastAPI(title="RozgarSetu")
class Req(BaseModel):
    resume: str
    jd: str
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/analyze")
def analyze(r: Req):
    g=gap(r.resume, r.jd)
    g["roadmap"]=learning_path(g["missing"])
    return g
