from .core import detect_craters
def demo(): print(detect_craters([{"x":0,"y":0,"r":10,"contrast":0.9}]))
if __name__=="__main__": demo()