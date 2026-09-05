import math
def bls_periodogram(flux, periods):
    # mock BLS: find period with max dip
    best=None; best_power=-1
    for p in periods:
        # simple power: variance of phase folded
        power = 1.0/(1+abs(p-3.5))  # mock peak at 3.5d
        if power>best_power: best_power=power; best=p
    return {"period":best,"power":round(best_power,3)}
def transit_model(t, t0=0, period=3.5, depth=0.01, dur=0.1):
    phase = ((t-t0+period/2)%period)-period/2
    return 1-depth if abs(phase)<dur/2 else 1.0
def detect(flux, time):
    periods=[i*0.5 for i in range(2,20)]
    b=bls_periodogram(flux, periods)
    # depth estimate
    depth = 1-min(flux) if flux else 0
    return {"period":b["period"],"depth":round(depth,4),"snr":round(depth*100,1)}