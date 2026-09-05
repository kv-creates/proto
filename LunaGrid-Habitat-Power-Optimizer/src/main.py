from .core import simulate
def demo(): print(simulate([5]*24, [3]*24)[:3])
if __name__=="__main__": demo()