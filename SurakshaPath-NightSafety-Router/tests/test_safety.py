from src.safety import segment_score, safest_path
def test_lighting_matters_at_night():
    good={"lighting":0.9,"crowd":0.8,"cctv":True,"police_dist_km":0.5}
    bad={"lighting":0.1,"crowd":0.1,"cctv":False,"police_dist_km":5}
    assert segment_score(good,22) > segment_score(bad,22)
    assert segment_score(good,14) > segment_score(bad,14)
def test_safest_avoids_dark():
    g={"A":[("B",{"lighting":0.9,"crowd":0.8,"cctv":True,"police_dist_km":0.5,"dist_km":1}),("C",{"lighting":0.2,"crowd":0.1,"cctv":False,"police_dist_km":3,"dist_km":0.6})],"B":[("D",{"lighting":0.8,"crowd":0.7,"cctv":True,"police_dist_km":1,"dist_km":1})],"C":[("D",{"lighting":0.1,"crowd":0.05,"cctv":False,"police_dist_km":4,"dist_km":0.7})],"D":[]}
    r=safest_path(g,"A","D",23)
    assert r["path"]==["A","B","D"]
