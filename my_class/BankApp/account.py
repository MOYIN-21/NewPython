# from BankApp.bank import Bank


class Account:
    # balance = 0
    # pin = None

    def __init__(self, account_number, account_name, pin):
        self.__account = account_number
        self.__account_name = account_name
        self.__pin = pin
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0 and amount is not int:
            self.__balance += amount
        else:
            ValueError("Insufficient fund")

    def get_account_number(self):
        return self.__account

    def get_account(self) -> str:
        return self.__account + " " + self.__account_name + " " + self.__pin

    def withdraw(self, amount: int, pin: str):
        try:
            if self.__pin == pin:
                if amount > 0:
                    if amount < self.__balance:
                        self.__balance -= amount
                    else:
                        raise ValueError("Insufficient fund")
            else:
                raise ValueError("WRONG PIN")
        except (ValueError, KeyboardInterrupt):
            print("Insufficient fund")

    def check_balance(self, pin):
        if self.__pin == pin:
            return self.__balance
        else:
            raise ValueError("Invalid pin")

    def change_pin(self, old_pin, new_pin):
        if self.__pin == old_pin:
            self.__pin = new_pin
            return new_pin






