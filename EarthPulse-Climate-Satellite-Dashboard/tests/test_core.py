from src.core import anomaly
def test_anom(): assert anomaly([1,1,1,1])["alert"]==False