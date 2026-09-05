def sharp_features(mag):
    # mag: {usflux, totpot}
    return {"r_value":mag.get("usflux",1)*0.001, "prob": min(0.9, mag.get("totpot",1)*0.0005)}
def predict(mag_series):
    probs=[sharp_features(m)["prob"] for m in mag_series]
    avg=sum(probs)/len(probs) if probs else 0
    cls="X" if avg>0.7 else "M" if avg>0.4 else "C"
    return {"prob":round(avg,3),"class":cls,"go_nogo":"NO-GO" if avg>0.6 else "GO"}