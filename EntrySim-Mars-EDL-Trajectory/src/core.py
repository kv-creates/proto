import math
def edl_sim(entry_v=5800, entry_angle=-12, mass=2000, cd=1.2, area=12):
    # 3-DOF simplified
    v=entry_v; h=125000; dt=1; g=3.71; rho0=0.02; H=11000
    t=0; max_q=0; max_g=0; traj=[]
    while h>0 and t<600:
        rho=rho0*math.exp(-h/H)
        drag=0.5*rho*v*v*cd*area/mass
        v-= (drag + g*math.sin(math.radians(-entry_angle)))*dt
        h-= v*math.sin(math.radians(-entry_angle))*dt
        q=0.5*rho*v*v
        max_q=max(max_q,q)
        max_g=max(max_g,drag/9.81)
        traj.append((t,h,v))
        t+=dt
        if v<500: break
    parachute = v<500 and h>5000
    return {"time":t,"max_q":round(max_q,1),"max_g":round(max_g,2),"parachute":parachute,"points":len(traj)}