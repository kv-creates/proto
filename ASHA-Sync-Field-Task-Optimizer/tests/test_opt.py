from src.optimizer import optimize
def test_o(): assert optimize([{"id":"a"}])["ordered"]==["a"]
