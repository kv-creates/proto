import pathlib, tempfile, os
import src.inventory as inv
def test_alerts(tmp_path, monkeypatch):
    monkeypatch.setattr(inv, "DB", tmp_path/"test.db")
    inv.init_db()
    import datetime
    today=datetime.date.today()
    inv.add_medicine("TestMed", 5, (today+datetime.timedelta(days=2)).isoformat(), 10)
    a=inv.alerts()
    assert any(x["medicine"]=="TestMed" for x in a)
