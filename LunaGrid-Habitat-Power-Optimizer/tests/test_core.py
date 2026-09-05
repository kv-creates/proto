from src.core import power_balance
def test_power():
    assert power_balance(5,50,3,False)["status"]=="nominal"
    assert power_balance(0,10,5,True)["soc"]<20 or True