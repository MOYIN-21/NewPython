import random
# from BankApp.account import *

from my_class.BankApp.account import Account


class Bank:
    pin = None
    balance = 0
    __account_list = []

    def __init__(self, bank):
        self.bank = bank
        self.__account_list = []

    def register_bank_account(self, first_name, last_name, pin):
        full_name = first_name + " " + last_name
        create_account = Account(self.generate_account_number(), full_name, pin)
        self.__account_list.append(create_account)

    def find_account(self, account_num):
        for account in self.__account_list:
            if account.get_account_number() == account_num:
                return account
        else:
            raise ValueError("Account does not exist")

    def deposit(self, amount, account_num):
        self.find_account(account_num).deposit(amount)

    def generate_account_number(self):
        # return "".join([str(random.randint(0, 9)) for num in range(10)])
        return str(len(self.__account_list) + 1)

    def withdraw(self, amount, account_num, pin):
            if amount > 0:
                self.find_account(account_num).withdraw(amount, pin)

    def transfer(self, amount: int, sender: str, receiver: str, pin:str):
        sender = self.find_account(str(sender))
        sender.withdraw(amount, pin)
        receiver = self.find_account(str(receiver))
        receiver.deposit(amount)

    def check_balance(self, account, pin):
        return self.find_account(account).check_balance(pin)

# p1 = Bank("a")
# print(p1.generate_account_number())