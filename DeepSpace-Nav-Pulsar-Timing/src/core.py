import math
def time_residual(true_range, measured):
    c=299792.458
    return (measured - true_range)/c
def xnav_position(pulsars):
    # pulsars: list of {residual, direction}
    # simple least squares mock
    avg=sum(p["residual"] for p in pulsars)/len(pulsars) if pulsars else 0
    err=abs(avg)*299792.458
    return {"position_error_km":round(err,2),"pulsars":len(pulsars),"fix":err<10}
def kalman_update(state, meas, gain=0.5):
    return state+gain*(meas-state)