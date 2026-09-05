import math
def coverage(sats, lat, lon):
    # sats: list of {a, inc, raan}
    vis=0
    for s in sats:
        # mock visibility: random but deterministic
        vis+= 1 if (hash(str(s))%10)>3 else 0
    return vis
def revisit(sats, target):
    cov=coverage(sats, target[0], target[1])
    return round(1440/max(1,cov),1)  # minutes
def optimize(num_planes, sats_per_plane, inc=53):
    sats=[]
    for p in range(num_planes):
        for s in range(sats_per_plane):
            sats.append({"a":550+6378,"inc":inc,"raan":p*360/num_planes})
    cov=coverage(sats,0,0)
    return {"sats":len(sats),"coverage":cov,"revisit_min":revisit(sats,(0,0))}