import math
PEST_SIG={"brown_planthopper":{"freq":4200},"stem_borer":{"freq":2800},"leaf_folder":{"freq":3500}}
def classify(wav_mock):
    f=wav_mock.get("peak_freq",0)
    best=None; bestd=1e9
    for k,v in PEST_SIG.items():
        d=abs(f-v["freq"])
        if d<bestd:
            bestd=d; best=k
    conf=max(0,1-bestd/2000)
    if conf<0.55:
        return {"pest":"none","confidence":round(conf,2),"risk":"low"}
    risk="high" if conf>0.8 else "medium"
    return {"pest":best,"confidence":round(conf,2),"risk":risk}
def outbreak_score(reports):
    if len(reports)<3:
        return {"cluster":False,"score":0.2}
    from collections import Counter
    c=Counter(r["pest"] for r in reports)
    top=c.most_common(1)[0]
    score=min(0.95,0.3+0.15*top[1])
    return {"cluster":top[1]>=3,"dominant_pest":top[0],"score":round(score,2)}
