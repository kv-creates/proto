from src.core import transmission
def test_h2o(): assert transmission({"1.4":0.002})["h2o"]==True