import math, statistics, datetime
from typing import List

def tds_status(tds):
    if tds<50: return "too_low_mineral"
    if tds<250: return "excellent"
    if tds<500: return "good_bis_limit"
    if tds<900: return "poor_high"
    return "unsafe_reject"

def leakage_detect(readings: List[float]):
    # readings: liters per 15min overnight 1am-4am (should be ~0)
    if not readings: return {"leak":None}
    mean=statistics.mean(readings)
    stdev=statistics.pstdev(readings) or 1
    # z>2 and mean>5L => leak
    z = (mean-0)/stdev
    return {"mean_l":round(mean,2), "z":round(z,2), "leak": mean>5 and z>1.5, "severity":"high" if mean>20 else "medium" if mean>5 else "none"}

def forecast_next7(history: List[float]):
    # simple linear + weekly seasonality mock
    if len(history)<7: return []
    # trend
    n=len(history)
    x=list(range(n))
    # linear regression slope
    mx=sum(x)/n; my=sum(history)/n
    num=sum((xi-mx)*(yi-my) for xi,yi in zip(x,history))
    den=sum((xi-mx)**2 for xi in x) or 1
    slope=num/den
    intercept=my - slope*mx
    out=[]
    for i in range(1,8):
        xi=n+i-1
        trend=intercept + slope*xi
        seasonal= 5*math.sin(2*math.pi*xi/7)
        out.append(round(max(0, trend+seasonal),1))
    return out

def tanker_need(daily_use_history, tank_capacity=5000, current_level=1200):
    fc=forecast_next7(daily_use_history)
    if not fc: return {}
    need=[]
    level=current_level
    for i, use in enumerate(fc):
        level-=use
        if level<500:
            need.append({"day":f"+{i+1}", "deficit_l": round(1000-level,1), "order_tanker": True})
            level+=4000  # tanker refill
        else:
            need.append({"day":f"+{i+1}", "deficit_l":0, "order_tanker": False})
    return {"forecast_l": fc, "plan": need}
