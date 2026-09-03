import statistics
def night_flow_leak(flows):
    m=statistics.mean(flows) if flows else 0
    return {"leak":m>5,"mean":round(m,2)}
