def transmission(depths):
    # depths: {wavelength: depth}
    # mock retrieval: H2O at 1.4um, CO2 at 4.3um
    h2o = depths.get("1.4",0)>0.001
    co2 = depths.get("4.3",0)>0.001
    ch4 = depths.get("3.3",0)>0.0005
    score = (0.4*h2o + 0.4*co2 + 0.2*ch4)
    biosig = h2o and ch4 and not co2
    return {"h2o":h2o,"co2":co2,"ch4":ch4,"habit_score":round(score,2),"biosignature":biosig}