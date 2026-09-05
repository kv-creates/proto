import statistics
def anomaly(series, window=12):
    if len(series)<window: return {"anomaly":0,"alert":False,"base":0,"cur":series[-1] if series else 0}
    base=statistics.mean(series[-window:])
    cur=series[-1]
    anom=(cur-base)/max(0.1,abs(base))
    return {"base":round(base,2),"cur":cur,"anomaly":round(anom,3),"alert":abs(anom)>0.2}
def fuse(ecostress, modis, grace):
    a1=anomaly(ecostress)["anomaly"]
    a2=anomaly(modis)["anomaly"]
    a3=anomaly(grace)["anomaly"]
    combined=(a1+a2+a3)/3
    return {"ecostress":a1,"modis":a2,"grace":a3,"combined":round(combined,3),"climate_alert":abs(combined)>0.15}