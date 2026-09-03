from src.rti import draft_rti
def test_dept():
    assert draft_rti("water supply")["dept"]=="water"
