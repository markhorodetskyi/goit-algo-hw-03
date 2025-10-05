from hw3.task_1 import get_days_from_today
from hw3.task_2 import input_params, get_numbers_ticket
from hw3.task_3 import normalize_phone

menu = (f"\n"
        f"Choose an option:\n"
        f"1. Task 1. Get days from today\n"
        f"2. Task 2. Ticket numbers\n"
        f"3. Task 3. Normalise phone numbers\n"
        f"""4 or press "Enter" to exit\n"""
        f"---------------------\n"
        f"Input a number from 1 to 4\n"
        f"Your choice: ")


def main():
    while True:
        menu_choice = input(menu)
        match menu_choice:
            case "1":
                date_input = input("Enter a date: ")
                try:
                    days = get_days_from_today(date_input)
                    print(f"Days from today: {days}")
                except ValueError as e:
                    print(e)

            case "2":
                try:
                    min_value, max_value, quantity = input_params()
                    ticket_numbers = get_numbers_ticket(min_value, max_value, quantity)
                    print(f"Generated ticket numbers: {ticket_numbers}")
                except ValueError as e:
                    print("Incorrect input. Please try again.")
                    print(f"Error: {e}")

            case "3":
                phone_numbers = [
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
                print(f"Example phone numbers: {phone_numbers}")
                try:
                    normalised_numbers = [normalize_phone(num) for num in phone_numbers]
                    print(f"Normalised phone numbers: {normalised_numbers}")
                except ValueError as e:
                    print(f"Error normalizing phone numbers: {e}")

            case "4":
                print("Exiting the program.")
                break

            case "":
                print("Exiting the program.")
                break

            case _:
                print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
