from src.core import bls_periodogram
def test_bls(): assert bls_periodogram([1,1],[1,2,3.5])["period"]==3.5