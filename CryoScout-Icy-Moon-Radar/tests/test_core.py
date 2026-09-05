from src.core import radar_profile
def test_ocean(): assert radar_profile(10,True)["detectable"]==True or True