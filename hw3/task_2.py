import random


def input_min_number() -> int:
    """
    Prompts the user to input a minimum number.
    :return: The minimum number as an integer.
    """
    while True:
        try:
            min_value = int(input("Enter the minimum number from 1 to 999 (inclusive): "))
            print(min_value)
            if min_value < 1 or min_value > 999:
                print("Minimum should be in range 1 to 999. Please try again.")
                continue
            return min_value
        except ValueError:
            print("Invalid input. Please enter an integer.")


def input_max_number(min_value: int) -> int:
    """
    Prompts the user to input a maximum number greater than the given minimum.
    :param min_value: The minimum number to compare against.
    :return: The maximum number as an integer.
    """
    while True:
        try:
            max_value = int(input(f"Enter the maximum number from {min_value + 1} to 1000 (inclusive): "))
            if max_value > 1000:
                print("Maximum should be less than or equal to 1000. Please try again.")
                continue
            if min_value >= max_value:
                print("Maximum should be greater than minimum. Please try again.")
                continue
            return max_value
        except ValueError:
            print("Invalid input. Please enter an integer.")


def input_quantity(min_value: int, max_value: int) -> int:
    """
    Prompts the user to input a quantity of unique numbers to generate.
    :param min_value: The minimum number in the range.
    :param max_value: The maximum number in the range.
    :return: The quantity of unique numbers as an integer.
    """
    while True:
        try:
            quantity = int(input(f"Enter the quantity of unique numbers to generate. Max quantity is {max_value - min_value + 1}: "))
            if quantity <= 0:
                print("Quantity should be a positive integer. Please try again.")
                continue
            if quantity > (max_value - min_value + 1):
                print("Quantity exceeds the range of unique numbers available. Please try again.")
                continue
            return quantity
        except ValueError:
            print("Invalid input. Please enter an integer.")


def input_params() -> tuple[int, int, int]:
    """
    Prompts the user to input minimum, maximum, and quantity values.
    :return: A tuple containing (min, max, quantity) as integers.
    """

    print("Please enter minimum, maximum, and quantity values. Min & Max should be in range 1 to 1000.")
    min_val = input_min_number()
    max_val = input_max_number(min_val)
    quantity = input_quantity(min_val, max_val)

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
