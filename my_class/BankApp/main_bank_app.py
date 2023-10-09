from my_class.BankApp.account import Account
from my_class.BankApp.bank import Bank


class ATMMachine:

    def __init__(self):
        self.EagleBank = ""
        self.userInput = 0
        self.firstName = ""
        self.lastName = ""
        self.pin = 0
        self.userAccount = ""
        self.balance = 0
        self.account = ""
        self.bank = Bank("EagleBank")
        self.bank1 = Account("Account number", "User", "pin")

    def main(self):
        self.main_menu()

    def main_menu(self):
        self.userInput = int(input(
            """WELCOME TO EAGLEBANK!
            Press:
            1 -> Open new account
            2 -> Deposit
            3 -> Withdraw
            4 -> Transfer
            5 -> Check balance
            6 -> Logout
            """))

        if self.userInput == 1:
            self.open_account()
        elif self.userInput == 2:
            self.deposit()
        elif self.userInput == 3:
            self.withdraw()
        elif self.userInput == 4:
            self.transfer()
        elif self.userInput == 5:
            self.check_balance()
        elif self.userInput == 6:
            self.logout()

    def check_balance(self):
        try:
            pin = input("Enter PIN: ")
            account_number = input("Enter account number: ")
            balance = self.bank.check_balance(account_number, pin)
            print(f"Balance: {balance}")

            raise ValueError
        except (ValueError, KeyboardInterrupt):
            self.main_menu()

    def transfer(self):
        try:
            pin_number = input("Enter pin number ")

            receiver_account_number = input("Enter receiver account number ")

            depositor_account_number = input("Enter depositor account number ")

            amount = int(input("Enter amount "))
            self.bank.transfer(amount, depositor_account_number, receiver_account_number, pin_number)

            print("Debit Alert: \nDear " + self.firstName + " " + self.lastName + ", you sent ", amount, " to "
                  + receiver_account_number)

            receiver = self.bank.find_account(receiver_account_number).get_account_name()

            print("Credit Alert: \nDear ", receiver, ", you received ", amount, " from " + depositor_account_number)

            raise ValueError
        except (ValueError, KeyboardInterrupt):
            self.main_menu()

    def withdraw(self):
        try:
            pin = input("Enter PIN: ")
            account_number = input("Enter account number: ")
            amount = int(input("Enter amount to withdraw: "))

            self.bank.withdraw(amount, account_number, pin)
            balance = self.bank.check_balance(account_number, pin)

            print(f"Account balance for {account_number} is ${balance}")
            self.main_menu()

            raise ValueError
        except (ValueError, KeyboardInterrupt):
            self.main_menu()

    def deposit(self):
        try:
            account_number = input("Enter account number: ")
            deposit_amount = float(input("Enter amount to deposit: "))

            self.bank.deposit(deposit_amount, account_number)
            self.bank1.deposit(deposit_amount)
            balance = deposit_amount

            print(f"Account balance for {account_number} is ${balance}")
            self.main_menu()

            raise ValueError
        except (ValueError, KeyboardInterrupt):
            self.main_menu()

    def open_account(self):
        try:
            self.firstName = input("Enter first name: ")
            self.lastName = input("Enter last name: ")
            self.pin = input("Create PIN: ")

            account_number = self.bank.register_bank_account(self.firstName, self.lastName, self.pin)

            print(f"Hello, {self.firstName} {self.lastName}")
            print("Welcome to Tranxactrust. We are happy to help you with safe online payments.")
            print(f"Your account ID is: {account_number}")
            print(f"Your Tranxactrust wallet ID number is: {account_number}")

            self.main_menu()
            raise ValueError
        except (ValueError, KeyboardInterrupt):
            self.main_menu()

    def logout(self):
        try:
            logout_option = input("Click yes to log out or no to return to app menu")
            if logout_option.capitalize() == "yes":
                self.main_menu()
            if logout_option.capitalize() == "no":
                exit(0)

            raise ValueError
        except (ValueError, KeyboardInterrupt):
            self.main_menu()


if __name__ == "__main__":
    machine = ATMMachine()
    machine.main()