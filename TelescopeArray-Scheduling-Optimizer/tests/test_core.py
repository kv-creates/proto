from src.core import schedule
def test_sched(): assert schedule([{"id":"a","priority":1,"duration":10,"sun":100}])["scheduled"]==1