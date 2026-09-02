from src.skills import gap
def test_coverage():
    g=gap("python sql", "python sql aws")
    assert g["coverage"]==66.7 or abs(g["coverage"]-66.7)<0.2
    assert "aws" in g["missing"]
