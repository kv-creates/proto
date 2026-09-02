from src.water import leakage_detect, tds_status
def test_leak():
    assert leakage_detect([0,0,1,0])["leak"]==False
    assert leakage_detect([12,15,18,14])["leak"]==True
def test_tds():
    assert tds_status(200)=="excellent"
    assert tds_status(1200)=="unsafe_reject"
