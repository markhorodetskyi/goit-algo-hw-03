from datetime import datetime, timedelta
import re


def check_date_format(date: str) -> datetime.date:
    """
    :param date: A string representing a date in one of the following formats:
    - 'YYYY-MM-DD'
    - 'DD.MM.YYYY'
    - 'YYYY/MM/DD'
    :return: A datetime.date object if the date is in a valid format, otherwise False.
    """
    pattern_1 = r'^\d{4}-\d{2}-\d{2}$'
    pattern_2 = r'^\d{2}\.\d{2}\.\d{4}$'
    pattern_3 = r'^\d{4}/\d{2}-/\d{2}$'

    if re.match(pattern_1, date):
        return datetime.strptime(date, '%Y-%m-%d').date()
    elif re.match(pattern_2, date):
        return datetime.strptime(date, '%d.%m.%Y')
    elif re.match(pattern_3, date):
        return datetime.strptime(date, '%Y/%m/%d')
    else:
        return False


def get_days_from_today(date: str) -> int:
    """
    :param date: A string representing a date
    :return: The number of days from today to the given date.
    """
    parsed_date = check_date_format(date)

    if not parsed_date:
        raise ValueError("Unknow date format. Please use 'YYYY-MM-DD', 'DD.MM.YYYY', or 'YYYY/MM/DD'.")

    today = datetime.today().date()
    delta = parsed_date - today
    return delta.days


