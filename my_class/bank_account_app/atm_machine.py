import sys


def create_account():
    pass


def main_menu():
    user = input("""WELCOME TO GTBANK
                Enter 1). To Create account
                      2). To Deposit
                      3). To Check Balance
                      4). To Transfer
                      5).To Withdraw
                      6). Exit
                      """)
    match user:
        case "1":
            create_account()
        case "2":
            deposit()
        case "3":
            check_balance()
        case "4":
            transfer()
        case "5":
            withdraw()
        case "6":
            exit_menu()
        case _:
            sys.exit(1)


def main_function():
    main_menu()