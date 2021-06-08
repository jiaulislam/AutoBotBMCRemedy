from utilites.make_data import make_downtime_from_open_time_2
from datetime import datetime

FORMAT = "%m/%d/%Y %I:%M:%S %p"

def test_downtime_1():
    _open_time = "6/6/2021 9:42:00 AM"
    date = make_downtime_from_open_time_2(_open_time, "6/6/2021 11:00:00 AM", "6/6/2021 11:45:00 AM")
    _cal_date = datetime.strptime(
        date, FORMAT 
    )
    _start_date = datetime.strptime(_open_time, FORMAT)
    assert divmod((_cal_date - _start_date).total_seconds(),60)[0] == 45

def test_downtime_2():
    _open_time = "6/6/2021 10:00:00 AM"
    date = make_downtime_from_open_time_2(_open_time, "6/6/2021 11:00:00 AM", "6/6/2021 2:00:00 PM")
    _cal_date = datetime.strptime(
        date, FORMAT 
    )
    _start_date = datetime.strptime(_open_time, FORMAT)
    assert divmod((_cal_date - _start_date).total_seconds(),60)[0] == 180

def test_downtime_3():
    _open_time = "6/6/2021 10:00:00 AM"
    date = make_downtime_from_open_time_2(_open_time, "6/6/2021 11:00:00 AM", "6/6/2021 2:00:00 PM")
    assert date == "06/06/2021 01:00:00 PM" 

def test_downtime_4():
    _open_time = "6/6/2021 10:00:00 AM"
    date = make_downtime_from_open_time_2(_open_time, "6/6/2021 11:00:00 AM", "6/6/2021 11:45:00 AM")
    assert date == "06/06/2021 10:45:00 AM" 