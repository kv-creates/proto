from fastapi import FastAPI, WebSocket
from .translator import stream_process, mock_translate
app=FastAPI(title="BhashaBridge")
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/translate")
def tr(body: dict):
    return {"translated": mock_translate(body.get("text",""), body.get("target","hi"))}
@app.websocket("/ws")
async def ws(ws: WebSocket):
    await ws.accept()
    while True:
        data=await ws.receive_text()
        # data: "en text|target"
        parts=data.split("|")
        text=parts[0]; target=parts[1] if len(parts)>1 else "hi"
        await ws.send_json({"en": text, "translated": mock_translate(text, target)})
