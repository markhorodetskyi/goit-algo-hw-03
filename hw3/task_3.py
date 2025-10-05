import re


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
        raise ValueError("Invalid phone number format.")