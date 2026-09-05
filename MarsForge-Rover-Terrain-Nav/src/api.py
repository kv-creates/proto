from fastapi import FastAPI
from .core import astar
app=FastAPI(title="MarsForge")
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/path")
def p(body: dict): return {"path":astar(body.get("elev",[[0,1],[1,0]]), tuple(body.get("start",[0,0])), tuple(body.get("goal",[1,1])))}
@app.get("/visual-data")
def v():
    elev=[[0,2,5],[1,3,4],[2,2,1]]
    return {"elev":elev,"path":astar(elev,(0,0),(2,2))}