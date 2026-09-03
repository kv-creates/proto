import datetime
RULES=[{"name":"GSTR-1","day":11,"penalty":50},{"name":"GSTR-3B","day":20,"penalty":50}]
def due_dates(year,month):
    return [{"task":r["name"],"due":datetime.date(year,month,r["day"]).isoformat()} for r in RULES]
def penalty(task,days):
    r=next((x for x in RULES if x["name"]==task),None)
    return r["penalty"]*days if r else 0
