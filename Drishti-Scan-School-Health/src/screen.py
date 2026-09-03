def vision_score(line):
    return {"refer":line<=4,"logMAR":round(0.1*(8-line),2)}
def bmi_percentile(age,bmi):
    median=15+0.3*age
    if bmi<median-2: return {"flag":"underweight"}
    if bmi>median+2: return {"flag":"overweight"}
    return {"flag":"normal"}
