def power_balance(solar_kw, battery_kwh, load_kw, eclipse=False):
    gen = 0 if eclipse else solar_kw
    net = gen - load_kw
    soc=battery_kwh
    if net>0:
        soc=min(100,soc+net*0.1)
    else:
        soc=max(0,soc+net*0.2)
    ok=soc>20
    return {"net_kw":round(net,2),"soc":round(soc,2),"status":"nominal" if ok else "critical"}
def thermal(rad_area, sun_flux, eclipse):
    q_in=0 if eclipse else sun_flux*0.7*rad_area*0.5
    q_out=rad_area*0.85*5.67e-8*(273**4)*0.001
    temp=273+(q_in-q_out)/1000
    return round(temp,1)
def simulate(solar_series, load_series):
    soc=50; out=[]
    for i,(s,l) in enumerate(zip(solar_series, load_series)):
        eclipse=(i%24)<6
        pb=power_balance(s,soc,l,eclipse)
        soc=pb["soc"]
        th=thermal(10, 1361 if not eclipse else 0, eclipse)
        out.append({"hour":i,"solar":s,"load":l,"soc":soc,"temp":th,"eclipse":eclipse})
    return out