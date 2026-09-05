import math
def lambert_dv(r1,r2,tof):
    mu=132712440018
    # mock porkchop: dv = |r2-r1|/tof * k
    dr=abs(r2-r1)
    dv=dr/max(1,tof)*0.5
    return round(dv,2)
def porkchop(r_earth, r_asteroid, tofs):
    out=[]
    for t in tofs:
        dv=lambert_dv(r_earth, r_asteroid, t)
        mass_return=1000*math.exp(-dv/3500)
        out.append({"tof":t,"dv":dv,"return_mass":round(mass_return,1)})
    best=min(out, key=lambda x: x["dv"])
    return {"porkchop":out,"best":best}