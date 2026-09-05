def visibility(target, sun_angle):
    return sun_angle>85 and sun_angle<135
def schedule(requests):
    # requests: [{id, priority, duration, sun}]
    # sort by priority, then greedy fit
    req=sorted(requests, key=lambda x: -x["priority"])
    timeline=[]; time=0
    for r in req:
        if visibility(r["id"], r["sun"]):
            timeline.append({"id":r["id"],"start":time,"end":time+r["duration"]})
            time+=r["duration"]+5  # slew
    return {"scheduled":len(timeline),"timeline":timeline,"eff":round(len(timeline)/max(1,len(requests)),2)}