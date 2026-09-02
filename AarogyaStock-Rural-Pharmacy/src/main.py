from .inventory import init_db, add_medicine, alerts, sms_sync_message, predict_stockout
import datetime
def demo():
    init_db()
    today = datetime.date.today()
    add_medicine("Paracetamol 500mg", 12, (today+datetime.timedelta(days=5)).isoformat(), 20)
    add_medicine("ORS", 100, (today+datetime.timedelta(days=200)).isoformat(), 15)
    add_medicine("Amoxicillin", 0, (today+datetime.timedelta(days=60)).isoformat(), 10)
    print("Alerts:", alerts())
    print("Predict:", predict_stockout())
    print("SMS:\n", sms_sync_message())
if __name__=="__main__": demo()
