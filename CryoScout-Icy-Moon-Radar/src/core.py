def radar_profile(ice_thickness_km, ocean=True):
    # mock two-way travel time
    v_ice=0.17  # km/us
    tt = 2*ice_thickness_km/v_ice
    ocean_echo = 0.8 if ocean else 0.1
    clutter = 0.2 if ice_thickness_km>15 else 0.5
    snr = ocean_echo/(clutter+0.1)
    return {"twtt_us":round(tt,1),"ocean_snr":round(snr,2),"detectable":snr>1.5}