from src.core import beam_efficiency
def test_eff(): assert beam_efficiency(1000)["eff"]>0