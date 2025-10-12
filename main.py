from datetime import datetime
from random import sample
import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]


def get_days_from_today(date: str) -> int | str:
    """
    Promt
    """
    try:
        parsed_date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        delta = parsed_date - today
        return int(delta.days)
    except ValueError:
        return "Unknow date format. Please use 'YYYY-MM-DD'"


def get_numbers_ticket(min_val: int, max_val: int, quantity: int) -> list[int]:
    """
    :param min_val: Minimum number in the range (inclusive).
    :param max_val: Maximum number in the range (inclusive).
    :param quantity: Number of unique random numbers to generate.
    :return: A sorted list of unique random numbers within the specified range.
    """
    if min_val < 1 or min_val > 999:
        return []
    if max_val <= min_val or max_val > 1000:
        return []
    if quantity <= 0 or quantity > (max_val - min_val + 1):
        return []

    numbers = list(sample(range(min_val, max_val + 1), quantity))
    numbers.sort()
    return numbers


def normalize_phone(phone_number: str) -> str:
    """
    :param phone_number: A string representing a phone number in various formats.
    :return: A normalized phone number in the format '+380XXXXXXXXX' or raises ValueError if invalid.
    """
    digits = re.sub(r'\D', '', phone_number)

    # Handle different cases based on the number of digits and prefixes
    if digits.startswith('0'):
        return '+380' + digits[1:]
    elif digits.startswith('380'):
        return '+' + digits
    elif digits.startswith('80'):
        return '+3' + digits[1:]
    else:
        print("Invalid phone number format.")


if __name__ == "__main__":
    print(get_days_from_today("2020.10.09"))
    print(get_numbers_ticket(299, 300, 3))
    print([normalize_phone(num) for num in raw_numbers])
