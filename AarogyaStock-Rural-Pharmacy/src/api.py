from flask import Flask, request, jsonify
from .inventory import init_db, add_medicine, consume, alerts, sms_sync_message, predict_stockout
app = Flask(__name__)
init_db()
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/medicine")
def add():
    d=request.json
    add_medicine(d["name"], int(d["stock"]), d["expiry"], int(d.get("threshold",20)))
    return {"ok":True}
@app.post("/consume")
def cons():
    d=request.json
    left=consume(d["name"], int(d["qty"]))
    return {"stock_left":left}
@app.get("/alerts")
def al(): return jsonify(alerts())
@app.get("/predict")
def pr(): return jsonify(predict_stockout())
@app.get("/sms-preview")
def sms(): return {"sms": sms_sync_message()}
if __name__=="__main__": app.run(port=8000, debug=True)
