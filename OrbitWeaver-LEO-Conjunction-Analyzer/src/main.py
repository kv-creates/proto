from .core import conjunction_report
def demo():
    print(conjunction_report({"a":7000,"inc":53}, {"a":7010,"inc":53}, [0,300,600]))
if __name__=="__main__": demo()