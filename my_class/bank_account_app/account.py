from Class_chinchin.exceptions import *


class Account:

    def __init__(self, account_number, account_name, pin):
        self.__account_name = account_name
        self.__account_number = account_number
        self.__pin = pin
        self.__balance = 0

    def check_balance(self, pin: int) -> int:
        self.validate_pin(pin)
        return self.__balance

    def deposit(self, amount: float) -> None:
        self.validate_amount(amount)
        self.__balance += amount

    def withdraw(self, amount, pin) -> None:
        self.validate_amount(amount)
        self.validate_pin(pin)
        self.__balance -= amount

    @staticmethod
    def validate_amount(amount: float):
        if amount < 0:
            raise NegativeAmountExceptions("AMOUNT CAN NOT BE NEGATIVE")

    def validate_amount_and_balance(self, amount):
        if amount > self.__balance:
            raise InsufficientFundException("INSUFFICIENT FUND")

    def validate_pin(self, pin: int):
        if self.__pin != pin:
            raise WrongPasswordException("INVALID PIN")
        else:
            return pin

    def account_number(self):
        return self.__account_number

    def get_account(self):
        return self.__account_number
