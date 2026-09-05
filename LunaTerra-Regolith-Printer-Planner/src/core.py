def layers(wall_h, layer_h=0.05):
    return int(wall_h/layer_h)
def mass(volume_m3, density=1500, ratio=0.6):
    return round(volume_m3*density*ratio,1)
def print_time(layers, speed_mps=0.1, perim=20):
    return round(layers*perim/speed_mps/3600,2)  # hours
def plan(hab):
    # hab: {wall_h, perim, volume}
    l=layers(hab.get("wall_h",3))
    m=mass(hab.get("volume",10))
    t=print_time(l, perim=hab.get("perim",30))
    return {"layers":l,"mass_kg":m,"hours":t,"isru_ratio":0.6}