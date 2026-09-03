from src.forecast import forecast
def test_f(): assert forecast([3000])["signal"] in ["wait","sell_now"]
