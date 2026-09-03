from src.segregator import classify_mock
def test_wet(): assert classify_mock({"h":60})["type"]=="wet"
