from .pest import classify, outbreak_score
def demo():
    print(classify({"peak_freq":4200}))
    print(outbreak_score([{"pest":"brown_planthopper","lat":19,"lon":72,"ts":"1"}]*3))
if __name__=="__main__": demo()
