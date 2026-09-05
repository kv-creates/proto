from src.core import detect_craters
def test_c(): assert detect_craters([{"r":10,"contrast":0.9}])["count"]==1