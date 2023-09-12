from Class_chinchin.exceptions import *
from my_class.bank_account_app.account import Account


class Bank:

    def __init__(self, bank_name: str):
        self.__bank_name = bank_name
        self.__list_account = []

    def register(self, first_name, last_name, pin):
        full_name = first_name + " " + last_name
        new_account = Account(self.generate_account_number(), full_name, pin)
        self.__list_account.append(new_account)

    def generate_account_number(self):
        return str(len(self.__list_account) + 1)

    def number_of_account(self):
        return len(self.__list_account)

    def find_account(self, account_number) -> str:
        for account in self.__list_account:
            if account.get_account_number() == account_number:
                return account
        else:
            raise AccountNotFoundException("ACCOUNT NOT FOUND")

    def deposit(self, amount, account_number):
        return self.find_account(account_number).deposit(amount)

    def check_balance(self, account_number, pin):
        return self.find_account(account_number).check_balance(pin)

    def with_draw(self, account_number, amount, pin):
        return self.find_account(account_number).withdraw(amount, pin)

    def transfer(self, amount: int, sender_account: str, receiver_account: str, pin: str):
        account_sender = self.find_account(str(sender_account))
        account_sender.withdraw(amount, pin)
        account_receiver = self.find_account(str(receiver_account))
        account_receiver.deposit(int(amount))
