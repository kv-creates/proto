from src.pest import classify, outbreak_score
def test_pest():
    assert classify({"peak_freq":4200})["pest"]=="brown_planthopper"
    assert classify({"peak_freq":100})["pest"]=="none"
