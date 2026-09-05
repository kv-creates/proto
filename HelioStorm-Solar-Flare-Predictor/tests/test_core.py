from src.core import predict
def test_go(): assert predict([{"usflux":0,"totpot":0}])["go_nogo"]=="GO"