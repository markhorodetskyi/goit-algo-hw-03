import random


def input_params() -> tuple[int, int, int]:
    """
    Prompts the user to input minimum, maximum, and quantity values.
    :return: A tuple containing (min, max, quantity) as integers.
    """
    min_value = ""
    max_value = ""
    quantity = ""

    while True:
        min_val = int(input("Enter the minimum number (inclusive): "))
        max_val = int(input("Enter the maximum number (inclusive): "))

        if min_val >= max_val:
            print("Minimum should be less than maximum. Please try again.")
            continue

        quantity = int(input("Enter the quantity of unique numbers to generate: "))

        if quantity <= 0:
            print("Quantity should be a positive integer. Please try again.")
            continue

        if quantity > (max_val - min_val + 1):
            print("Quantity exceeds the range of unique numbers available. Please try again.")
            continue

        break

    return min_val, max_val, quantity


def get_numbers_ticket(min_val: int, max_val: int, quantity: int) -> list[int]:
    """
    :param min_val: Minimum number in the range (inclusive).
    :param max_val: Maximum number in the range (inclusive).
    :param quantity: Number of unique random numbers to generate.
    :return: A sorted list of unique random numbers within the specified range.
    """
    numbers = list(random.sample(range(min_val, max_val + 1), quantity))
    numbers.sort()
    return numbers
