import re
from datetime import datetime as DateTime
from datetime import timedelta
from typing import List

"""
Format the Date with standard requirement. All five task
data is formatted through this python file & the relationship
query string generator also.

written by: jiaul_islam
"""


def get_change_start_time(m_date: str) -> str:
    """ Get the Change Start Time """
    make_date_time = parse_datetime(m_date)
    if date_valid(make_date_time):
        make_date_time += timedelta(days=1)
    start_time = make_date_time.replace(hour=9, minute=0, second=0)
    return start_time.strftime('%m/%d/%Y %I:%M:%S %p')


def get_service_start_downtime(m_date: str) -> str:
    """ Get the Change Start downtime """
    make_date_time = parse_datetime(m_date)
    if date_valid(make_date_time):
        make_date_time += timedelta(days=1)
    start_downtime = make_date_time.replace(hour=11, minute=0, second=0)
    return start_downtime.strftime('%m/%d/%Y %I:%M:%S %p')


def get_service_end_downtime(start_downtime: str, duration: str) -> str:
    """ Get the Change End Time """
    make_date_time = DateTime.strptime(
        str(start_downtime), '%m/%d/%Y %I:%M:%S %p')

    if date_valid(make_date_time):
        make_date_time += timedelta(days=1)

    parse_duration = duration[:5]
    hour = int(parse_duration[:2])
    minute = int(parse_duration[3:5])

    if hour == 0 and minute == 30:
        make_date_time += timedelta(minutes=30)
    elif hour == 0 and minute == 45:
        make_date_time += timedelta(minutes=45)
    else:
        make_date_time += timedelta(hours=hour)
    return make_date_time.strftime('%m/%d/%Y %I:%M:%S %p')


def get_change_close_start_time(m_date: str) -> str:
    """ Get the Change Close Start Time """
    make_date_time = parse_datetime(m_date)

    if date_valid(make_date_time):
        make_date_time += timedelta(days=1)

    close_start_time = make_date_time.replace(hour=17, minute=0, second=0)
    return close_start_time.strftime('%m/%d/%Y %I:%M:%S %p')


def get_change_close_end_time(m_date: str) -> str:
    """ Get the Change Close End Time """
    make_date_time = parse_datetime(m_date)

    if date_valid(make_date_time):
        make_date_time += timedelta(days=1)

    close_start_time = make_date_time.replace(hour=18, minute=0, second=0)
    return close_start_time.strftime('%m/%d/%Y %I:%M:%S %p')


def parse_datetime(m_date: str) -> DateTime:
    """ Get the as a formatted as required """
    return DateTime.strptime(str(m_date), '%Y-%m-%d %H:%M:%S')


def split_string(AnyStr: str) -> List[str]:
    """ Split the Given site codes with comma(,) semi-colon(;) backslash(/) forwardslash(\\) hipen(-) string """
    _PATTERN = r'\b[A-Z]{3}[A-Z0-9]{3}[0-9]{1}\b'
    _list_of_sites: List[str] = re.findall(_PATTERN, AnyStr)
    return _list_of_sites


def make_impact_list(site_list: str) -> str:
    """ Export a file with site list & return the string of site list with formatted impact list """
    _list_of_sites: List[str] = split_string(site_list)
    _IMPACT_LIST = "\n\nImpact List:"

    return f"{_IMPACT_LIST} {','.join(_list_of_sites)}"


def list_of_change(file_name: str) -> List[str]:
    """ return the list of Change Numbers from the text file """
    change_list = []
    try:
        with open(file_name, "r") as file:
            for change in file:
                change = change[:15]
                change.strip()
                change_list.append(change)
    except FileNotFoundError as error:
        print(f"\n{error}")

    return change_list


def get_current_system_time() -> str:
    """ parse the current system time with formatted string """
    current_time = DateTime.now()
    return current_time.strftime("%m/%d/%Y %I:%M %p")


def make_downtime_from_open_time(open_time: str) -> str:
    """ make and return e downtime duration with the help of open time """
    original_date = DateTime.strptime(
        open_time, "%m/%d/%Y %I:%M:%S %p")
    # add extra 30 minute with the parsed time to close for service effective NCR
    original_date += timedelta(minutes=30)

    return str(original_date.strftime("%m/%d/%Y %I:%M:%S %p"))

def make_downtime_from_open_time_2(open_time: str, schedule_start_time: str, schedule_end_time: str):
    _original_date = DateTime.strptime(
        open_time, "%m/%d/%Y %I:%M:%S %p")
    _start_date = DateTime.strptime(
        schedule_start_time, "%m/%d/%Y %I:%M:%S %p"
    )
    _end_date = DateTime.strptime(
        schedule_end_time, "%m/%d/%Y %I:%M:%S %p"
    )
    _time_diff = divmod((_end_date - _start_date).total_seconds(),60)
    _original_date += timedelta(minutes=_time_diff[0])

    return _original_date.strftime("%m/%d/%Y %I:%M:%S %p")


def make_query_string(site_string: str) -> str:
    """ Generate the query_list string for relationship addition """
    sites: List[str] = split_string(site_string)
    query_list: list = []
    invalid_list: list = []
    for site in sites:
        if len(site.strip()) == 7:
            query_list.append(f"'Name'LIKE\"%{site.strip()}\"")
        else:
            invalid_list.append(site.strip())

    if len(invalid_list):
        print(f"Invalid Site Codes: {invalid_list}\n")

    return "OR".join(query_list)


def date_valid(user_date: DateTime, system_date: DateTime = DateTime.today()) -> bool:
    """ Check if the date is valid as per BMC Regulation """
    if user_date <= system_date:
        return True
    else:
        return False
