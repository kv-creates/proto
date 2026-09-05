from .core import schedule
def demo(): print(schedule([{"id":"a","priority":1,"duration":10,"sun":100}]))
if __name__=="__main__": demo()