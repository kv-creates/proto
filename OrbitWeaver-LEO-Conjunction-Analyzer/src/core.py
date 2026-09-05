import math
MU=398600.4418
R_E=6378.137
def propagate_circular(a_km, inc_deg, t_sec):
    n = math.sqrt(MU / a_km**3)
    # simple circular equatorial + inclination
    x = a_km*math.cos(n*t_sec)
    y = a_km*math.sin(n*t_sec)*math.cos(math.radians(inc_deg))
    z = a_km*math.sin(n*t_sec)*math.sin(math.radians(inc_deg))
    return (x,y,z)
def miss_distance(r1, r2):
    return math.sqrt(sum((a-b)**2 for a,b in zip(r1,r2)))
def alfano_pc(miss_km, cov1=0.1, cov2=0.1):
    # simplified Pc: exp(-miss^2/(2*var))
    var = cov1+cov2
    pc = math.exp(-miss_km**2/(2*var)) * 0.01
    return round(min(0.99, pc),6)
def conjunction_report(tle1, tle2, times):
    a1=tle1.get('a', 7000); a2=tle2.get('a',7010); inc1=tle1.get('inc',53); inc2=tle2.get('inc',53)
    out=[]
    for t in times:
        r1=propagate_circular(a1, inc1, t)
        r2=propagate_circular(a2, inc2, t)
        md=miss_distance(r1,r2)
        pc=alfano_pc(md)
        out.append({"t":t,"miss_km":round(md,3),"pc":pc,"risk":"high" if pc>0.001 else "low"})
    return out