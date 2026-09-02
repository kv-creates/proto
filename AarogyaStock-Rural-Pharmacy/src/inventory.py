import sqlite3, datetime, pathlib
DB = pathlib.Path("data.db")
def init_db():
    con = sqlite3.connect(DB)
    con.execute("""CREATE TABLE IF NOT EXISTS medicines (
        id INTEGER PRIMARY KEY, name TEXT UNIQUE, stock INTEGER, expiry TEXT, threshold INTEGER, last_sync TEXT
    )""")
    con.commit(); con.close()
def add_medicine(name, stock, expiry, threshold=20):
    con = sqlite3.connect(DB)
    con.execute("INSERT OR REPLACE INTO medicines(name,stock,expiry,threshold,last_sync) VALUES (?,?,?,?,?)",
                (name, stock, expiry, threshold, datetime.datetime.now().isoformat()))
    con.commit(); con.close()
def consume(name, qty):
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("SELECT stock FROM medicines WHERE name=?", (name,))
    row = cur.fetchone()
    if not row: raise ValueError("not found")
    new = row[0]-qty
    cur.execute("UPDATE medicines SET stock=? WHERE name=?", (new, name))
    con.commit(); con.close()
    return new
def alerts():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    today = datetime.date.today()
    alerts=[]
    for name, stock, expiry, thr in cur.execute("SELECT name,stock,expiry,threshold FROM medicines"):
        try:
            exp = datetime.date.fromisoformat(expiry)
            days = (exp - today).days
            if days < 30:
                alerts.append({"type":"expiry","medicine":name,"days_left":days,"severity":"high" if days<7 else "medium"})
        except: pass
        if stock <= thr:
            alerts.append({"type":"stockout","medicine":name,"stock":stock,"threshold":thr,"severity":"high" if stock==0 else "medium"})
    con.close()
    return sorted(alerts, key=lambda x: (x["severity"]!="high", x["type"]))
def predict_stockout(days_window=7, avg_daily_use=2):
    con = sqlite3.connect(DB)
    res=[]
    for name, stock in con.execute("SELECT name,stock FROM medicines"):
        days_left = stock // max(1, avg_daily_use)
        if days_left <= days_window:
            res.append({"medicine":name,"stock":stock,"days_left":int(days_left),"need_reorder":True})
    con.close()
    return res
def sms_sync_message():
    a = alerts()
    if not a: return "AarogyaStock: All stocks OK."
    lines = ["AarogyaStock ALERT:"]
    for al in a[:5]:
        if al["type"]=="expiry": lines.append(f"EXPIRY {al['medicine']} in {al['days_left']}d")
        else: lines.append(f"LOW {al['medicine']} stock {al['stock']}")
    return "\n".join(lines)
