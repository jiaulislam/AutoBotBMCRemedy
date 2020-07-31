import datetime

"""
Format the Date with standard requirement. All five task
data is formatted through this python file.
"""


def get_change_start_time(m_date):
    """ Get the Change Start Time """
    make_date_time = parse_datetime(m_date)
    if make_date_time <= datetime.datetime.today():
        make_date_time += datetime.timedelta(days=1)
    start_time = make_date_time.replace(hour=9, minute=0, second=0)
    return start_time.strftime('%m/%d/%Y %I:%M:%S %p')


def get_service_start_downtime(m_date):
    """ Get the Change Start downtime """
    make_date_time = parse_datetime(m_date)
    start_downtime = make_date_time.replace(hour=11, minute=0, second=0)
    return start_downtime.strftime('%m/%d/%Y %I:%M:%S %p')


def get_service_end_downtime(start_downtime, duration):
    """ Get the Change End Time """
    make_date_time = datetime.datetime.strptime(str(start_downtime), '%m/%d/%Y %I:%M:%S %p')

    parse_duration = duration[:5]
    hour = int(parse_duration[:2])
    minute = int(parse_duration[3:5])

    if hour == 0 and minute == 30:
        make_date_time += datetime.timedelta(minutes=30)
    elif hour == 0 and minute == 45:
        make_date_time += datetime.timedelta(minutes=45)
    else:
        make_date_time += datetime.timedelta(hours=hour)
    return make_date_time.strftime('%m/%d/%Y %I:%M:%S %p')


def get_change_close_start_time(m_date):
    """ Get the Change Close Start Time """
    make_date_time = parse_datetime(m_date)
    close_start_time = make_date_time.replace(hour=17, minute=0, second=0)
    return close_start_time.strftime('%m/%d/%Y %I:%M:%S %p')


def get_change_close_end_time(m_date):
    """ Get the Change Close End Time """
    make_date_time = parse_datetime(m_date)
    close_start_time = make_date_time.replace(hour=18, minute=0, second=0)
    return close_start_time.strftime('%m/%d/%Y %I:%M:%S %p')


def parse_datetime(m_date):
    """ Get the as a formatted as required """
    return datetime.datetime.strptime(str(m_date), '%Y-%m-%d %H:%M:%S')


def make_impact_list(site_list, site_group):
    """ Export a file with site list & return the string of site list with formatted impact list """
    ctr = 0
    file_name = site_group + '.txt'
    sites = site_list.split(',')
    impact_list = "Impact List: "

    with open(file_name, 'w+') as notepad_file:
        for site in sites:
            impact_list += site
            notepad_file.write(site.strip())
            notepad_file.write("\n")
            if ctr != len(sites) - 1:
                impact_list += ','
                ctr += 1
        notepad_file.close()
    return "\n\n" + impact_list


def list_of_change(file_name):
    """ return the list of Change Numbers from the text file """
    change_list = []
    try:
        with open(file_name) as file:
            for change in file:
                change = change[:15]
                change.strip()
                change_list.append(change)
    except FileNotFoundError as error:
        print(f"\n{error}")

    return change_list


def get_current_system_time():
    """ parse the current system time with formatted string """
    current_time = datetime.datetime.now()
    return current_time.strftime("%m/%d/%Y %I:%M %p")

def make_downtime_from_open_time(open_time: str):
    """ make and return e downtime duration with the help of open time """
    original_date = datetime.datetime.strptime(
        open_time, "%m/%d/%Y %I:%M:%S %p")
    # add extra 30 minute with the parsed time to close for service effective NCR
    original_date += datetime.timedelta(minutes=30)

    return str(original_date.strftime("%m/%d/%Y %I:%M:%S %p"))
