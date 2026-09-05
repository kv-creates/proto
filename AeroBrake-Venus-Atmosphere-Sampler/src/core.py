import math
def heating(v, rho, nose_r=1):
    return 1.83e-4*math.sqrt(rho/nose_r)*v**3
def aerocapture(v_inf, peri_km):
    rho=65*math.exp(-peri_km/15)  # Venus approx
    q=heating(v_inf*1000, rho)
    g= (v_inf*1000)**2/(peri_km*1000+6052*1000)/9.81
    ok= q<500 and g<15
    return {"q_w_cm2":round(q,1),"g":round(g,1),"capture":ok}