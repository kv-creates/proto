from src.core import miss_distance, alfano_pc, propagate_circular
def test_miss():
    assert miss_distance((0,0,0),(3,4,0))==5
def test_pc():
    assert alfano_pc(0)>alfano_pc(10)
def test_prop():
    x,y,z=propagate_circular(7000,53,0)
    assert abs(x-7000)<1