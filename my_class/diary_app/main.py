import sys
from datetime import time

from my_class.diary_app.diary import *

my_dairy = Diary


def main_function():
    main_menu()


def create_diary():
    user_name = str(input("Enter your name\n"))
    password = input("Enter password or pin\n")
    mydairy = Diary(user_name, password)
    print(f"""DIARY CREATED SUCCESSFULLY
    Dear {user_name}, your password is {password}""")
    diary_menu()


def login_diary():
    password = input("Enter password")
    Diary.unlock_diary(password)
    diary_menu()


def create_entry():
    Id = input("Enter id\n")
    title = input("Enter title\n")
    bodys = input("Enter body\n")
    my_dairy.create_entry(Id, title, bodys)
    print("Entry created successfully")


def find_entry():
    id = int(input("Enter diary id\n"))
    Diary.find_entry_by_id(id)
    delete_entry()


def delete_entry():
    id = int(input("Enter your id\n"))
    Diary.delete_entry(id)
    update_entry()


def update_entry():
    id = int(input("Enter id\n"))
    title = str(input("Enter title\n"))
    body = str(input("Enter body\n"))
    Diary.update_entry(id, title, body)


def diary_menu():
    user = input("""
    1 ->Create Entry
    2 ->Find Entry
    3 ->Delete Entry
    4 ->Update Entry
    7 ->Exit
    \n""")
    match user:
        case "1":
            create_entry()
        case "2":
            find_entry()
        case "3":
            delete_entry()
        case "4":
            update_entry()
        case "7":
            exit_diary()
        case _:
            sys.exit(1)


def exit_diary():
    sys.exit(0)


def main_menu():
    user = input("""
                Welcome to Diary
                1 -> Create Diary
                2 -> Login Diary
                3 -> Exit Diary
                """)
    match user:
        case "1":
            create_diary()
        case "2":
            login_diary()
        case "3":
            exit_diary()
        case _:
            sys.exit(1)


if __name__ == "__main__":
    print(main_function())
