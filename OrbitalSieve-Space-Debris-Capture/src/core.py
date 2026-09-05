def delta_v(a1,a2):
    import math
    mu=398600; r1=a1; r2=a2
    dv=math.sqrt(mu/r1)* (math.sqrt(2*r2/(r1+r2))-1)
    return round(abs(dv)*2,1)  # round trip
def capture_window(debris_spin):
    return "grapple" if debris_spin<5 else "harpoon" if debris_spin<20 else "net"
def plan(debris):
    # debris: {a, spin, mass}
    dv=delta_v(7000, debris.get("a",7200))
    win=capture_window(debris.get("spin",3))
    deorbit=50 if debris.get("mass",100)<500 else 120
    return {"dv_mps":dv,"method":win,"deorbit_dv":deorbit,"total":dv+deorbit}