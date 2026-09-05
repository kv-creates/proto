from src.core import astar
def test_path(): assert astar([[0,1],[1,0]],(0,0),(1,1)) is not None