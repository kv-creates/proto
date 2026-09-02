from src.translator import mock_translate, stream_process
def test_hi():
    assert "नमस्ते" in mock_translate("hello", "hi")
def test_stream():
    assert len(stream_process(["hello","today we will learn about"], "hi"))==2
