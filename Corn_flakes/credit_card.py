def main():
    credit_card_number = input("Enter a credit card number: ")

    card_type = get_card_type(credit_card_number)
    is_valid = is_valid_credit_card_number(credit_card_number)
    calculate_index(credit_card_number)

    print("Credit Card Type:", card_type)
    print("Validity Status:", "Valid" if is_valid else "Invalid")


def get_card_type(credit_card_number):
    if credit_card_number.startswith("4"):
        return "Visa"
    elif credit_card_number.startswith("5"):
        return "MasterCard"
    elif credit_card_number.startswith("37"):
        return "American Express"
    elif credit_card_number.startswith("6"):
        return "Discover"
    else:
        return "Unknown"


def is_valid_credit_card_number(credit_card_number):
    total_sum = 0
    alternate = False
    for digit in credit_card_number[::-1]:
        digit = int(digit)
    if alternate:
        digit *= 2
    if digit > 9:
        digit = digit % 10 + 1
        total_sum += digit
    alternate = not alternate
    return total_sum % 10 == 0


def calculate_index(credit_card_number):
    card_length = len(credit_card_number)
    print("Credit card index:", card_length)


if __name__ == "__main__":
    main()
