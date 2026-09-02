"""
Safety scoring for road segments.
Score = 0.4*lighting +0.3*crowd +0.2*cctv +0.1*police + time_penalty
"""
import math, heapq
from typing import Dict, List, Tuple

def segment_score(seg: Dict, hour: int) -> float:
    # seg: {lighting 0-1, crowd 0-1, cctv bool, police_dist_km}
    lighting = seg.get("lighting", 0.5)
    crowd = seg.get("crowd", 0.5)
    cctv = 1.0 if seg.get("cctv") else 0.0
    police = max(0, 1 - seg.get("police_dist_km", 2)/3)
    base = 0.4*lighting + 0.3*crowd + 0.2*cctv + 0.1*police
    # night penalty 9pm-4am
    night_factor = 1.0
    if 21 <= hour <= 23 or 0 <= hour <= 4:
        night_factor = 0.6 + 0.4*lighting  # lighting matters more at night
        # need crowd at night
        night_factor *= (0.7 + 0.3*crowd)
    safety = base * night_factor
    return round(max(0, min(1, safety)), 3)

def route_safety(route_segments: List[Dict], hour: int) -> Dict:
    scores = [segment_score(s, hour) for s in route_segments]
    avg = sum(scores)/len(scores) if scores else 0
    min_s = min(scores) if scores else 0
    # weighted: avg 70% + min 30% (avoid one bad stretch)
    overall = 0.7*avg + 0.3*min_s
    label = "safe" if overall>0.7 else "moderate" if overall>0.45 else "avoid"
    return {"overall": round(overall,3), "avg": round(avg,3), "min": round(min_s,3), "label": label, "segments": scores}

# Graph routing demo with Dijkstra maximizing safety-adjusted weight
def safest_path(graph: Dict[str, List[Tuple[str, Dict]]], start: str, end: str, hour: int):
    # graph: node -> [(neighbor, segment_meta)]
    # weight = distance / (safety+0.3) -> prefer safe even if longer
    dist = {start: 0}
    prev = {}
    pq = [(0, start)]
    visited=set()
    while pq:
        d,u = heapq.heappop(pq)
        if u in visited: continue
        visited.add(u)
        if u==end: break
        for v, seg in graph.get(u, []):
            s = segment_score(seg, hour)
            w = seg.get("dist_km",1) / (s + 0.3)
            nd = d + w
            if nd < dist.get(v, math.inf):
                dist[v]=nd
                prev[v]=u
                heapq.heappush(pq,(nd,v))
    if end not in prev and end!=start:
        return None
    # reconstruct
    path=[end]
    while path[-1]!=start:
        path.append(prev[path[-1]])
    path.reverse()
    return {"path": path, "cost": round(dist[end],3)}

if __name__=="__main__":
    g={"A":[("B",{"lighting":0.9,"crowd":0.8,"cctv":True,"police_dist_km":0.5,"dist_km":1}),("C",{"lighting":0.2,"crowd":0.1,"cctv":False,"police_dist_km":3,"dist_km":0.6})],"B":[("D",{"lighting":0.8,"crowd":0.7,"cctv":True,"police_dist_km":1,"dist_km":1})],"C":[("D",{"lighting":0.1,"crowd":0.05,"cctv":False,"police_dist_km":4,"dist_km":0.7})],"D":[]}
    print(safest_path(g,"A","D",22))
    print(route_safety([{"lighting":0.9,"crowd":0.8,"cctv":True,"police_dist_km":0.5},{"lighting":0.2,"crowd":0.1,"cctv":False,"police_dist_km":3}],22))
