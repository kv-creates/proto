from .water import tds_status, leakage_detect, tanker_need
def demo():
    print("TDS 380:", tds_status(380))
    print("Leak:", leakage_detect([1,0,2,1,0,12,18,15]))  # leak
    print("No leak:", leakage_detect([0,1,0,0,1,0]))
    hist=[820,900,850,880,920,870,890,910,930,860,880,900,950,900]
    print(tanker_need(hist, 5000, 1200))
if __name__=="__main__": demo()
