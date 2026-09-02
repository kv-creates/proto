from .safety import segment_score, route_safety, safest_path
import json
def demo():
    print(json.dumps(safest_path({"A":[("B",{"lighting":0.9,"crowd":0.8,"cctv":True,"police_dist_km":0.5,"dist_km":1}),("C",{"lighting":0.2,"crowd":0.1,"cctv":False,"police_dist_km":3,"dist_km":0.6})],"B":[("D",{"lighting":0.8,"crowd":0.7,"cctv":True,"police_dist_km":1,"dist_km":1})],"C":[("D",{"lighting":0.1,"crowd":0.05,"cctv":False,"police_dist_km":4,"dist_km":0.7})],"D":[]}, "A","D",22), indent=2))
if __name__=="__main__": demo()
