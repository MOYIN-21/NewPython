from datetime import datetime
from random import random
import re

from my_class.diary_app.Diary import Diary


class MainDiary:

    def __init__(self):
        self.username = ""
        self.password = ""
        self.title = ""
        self.body = ""
        self.diaryUser = 0
        self.token = ""
        self.bodyEdited = ""
        self.titleEdited = ""
        self.id = 0
        self.currentDateTime = datetime.now()
        self.diary = Diaries()

    def main(self):
        self.welcome_menu()
        self.diary_menu()
        self.lock_diary()

    def welcome_menu(self):
        self.diaryUser = int(input("""
        ===================================
            HELLO MY LOVEY DOVEY! WELCOME TO EAGLE DIARY

            1. Create new diary account

            2. Log in

            3. Exit
        ===================================    
        """))
        match self.diaryUser:
            case 1 :
                self.create_account()
            case 2:
                self.login()
            case 3:
                self.exit_diary()
            case other:
                exit(0)

    def exit_diary(self):
        exit_option = input("Click yes to log out or no to return to Diary menu: ")
        if exit_option.lower() == 'yes':
            print(":( Buddy Diary is closing>>>>\nGoodbye!")
            exit(0)
        elif exit_option.lower() == 'no':
            self.welcome_menu()
        else:
            self.exit_diary()

    def login(self):
        try:
            user_login = input("Enter username: ")
            user_password = input("Enter password: ")

            if self.username != user_login:
                print("Username does not exist")
                if self.password != user_password:
                    print("Invalid password")
        except Exception as error:
            print(error)
            self.welcome_menu()
        self.diary_menu()

    def diary_menu(self):
        self.diaryUser = int(input("""
        ===================================
            To continue, press:
            
            1. Create entry
            2. Delete entry
            3. Find entry by ID
            4. Update entry
            5. Logout
        ===================================    
        """))
        if self.diaryUser == 1:
            self.create_entry()
        elif self.diaryUser == 2:
            self.delete_entry()
        elif self.diaryUser == 3:
            self.find_entry_by_id()
        elif self.diaryUser == 4:
            self.update_entry()
        elif self.diaryUser == 5:
            self.logout()
        else:
            exit(0)

    def logout(self):
        logout_option = input("Click yes to log out or no to return to Diary menu: ")
        if logout_option.lower() == 'yes':
            self.welcome_menu()
        elif logout_option.lower() == 'no':
            self.diary_menu()
        else:
            exit(0)

    def update_entry(self):
        get_id = int(input("Enter entry ID to update: "))
        if get_id == 0:
            self.update_entry()
            raise Exception("Entry not found")
        self.diary.find_by_user_name(self.username).find_entry_by_id(get_id).get_diary_info()
        self.diary.find_by_user_name(self.username).update_entry(get_id, self.title, self.body)

        edit_title = input("Enter yes to edit title: ")
        if edit_title.lower() == "yes":
            print(self.title)
            self.titleEdited = input("Edit: ")
        else:
            self.update_entry()

        if not self.titleEdited or self.titleEdited.lower() == "no":
            self.titleEdited = self.title

        edit_body = input("Enter yes to edit body: ")
        if edit_body.lower() == "yes":
            print(self.body)
            self.bodyEdited = input("Edit: ")

        if not self.bodyEdited or self.bodyEdited.lower() == "no":
            self.bodyEdited = self.body

        print("Entry successfully updated.")

        confirm_update = int(input("Enter entry ID to see entry update: "))
        self.diary.find_by_user_name(self.username).find_entry_by_id(confirm_update).get_diary_info()
        print(
            f"Entry successfully updated with new title as: \"{self.titleEdited}\" "
            f"and new body as: \"{self.bodyEdited}\" on {self.currentDateTime}")
        self.diary_menu()

    def find_entry_by_id(self):
        id = int(input("Enter entry ID: "))
        if id == 0:
            print("Invalid ID")
            navigate = input("Enter Yes to retry or No to go to Diary menu: ")
            if navigate.lower() == 'yes':
                self.find_entry_by_id()
            elif navigate.lower() == 'no':
                self.diary_menu()
        self.diary.find_by_user_name(self.username).find_entry_by_id(id).get_diary_info()
        print("Entry found")
        print(self.title)
        print(self.body)
        self.diary_menu()

    def delete_entry(self):
        id = int(input("Enter id to delete entry: "))
        if self.ID != id:
            print("Invalid ID")
            self.delete_entry()
        self.diary.find_by_user_name(self.username).delete_entry(self.ID)
        confirm = input("You are about to delete this entry. Enter yes to continue: ")
        if confirm.lower() == "yes":
            print(self.title)
            print(self.body)
            print("Deleting>>>>\nEntry deleted successfully")
        elif confirm.lower() == "no":
            self.diary_menu()
        self.diary_menu()

    def create_entry(self):
        self.title = input("Create title: ")
        self.body = input("Write body: ")

        if not self.title or not self.body:
            raise (ValueError, KeyboardInterrupt, "Title or body must be entered")

        self.diary.find_by_user_name(self.username).create_entry(self.title, self.body)
        print(
            f"Entry successfully created with title as: \"{self.title}\" "
            f"and body as: \"{self.body}\" on {self.currentDateTime}")
        self.diary_menu()


    def create_account(self):
        user = input("Enter username: ")
        if user.isalpha():
            self.username = user

        security = input("Enter password: ")
        if user.isalpha():
            self.password = security

        if not user:
            print("Username cannot be blank.")
            self.create_account()

        if not security:
            print("Password cannot be blank.")
            self.create_account()

        self.diary.add_user(self.username, self.password)
        name = f"Hello {self.username}, your account has been created successfully. You are welcome to use your diary."
        print(name)
        self.diary_menu()
































class Diaries:

        def __init__(self):
            self.diary = Diary
            self.diaries = []

        def add_user(self, username, password):
            diary = Diary(username, password)
            self.diaries.append(diary)

        def find_by_user_name(self, username):
            for self.diary in self.diaries:
                if self.diary.get_username() == username:
                    return self.diary
                raise ValueError("Username not found")

        def delete(self, username, password):
            diary = Diary(username, password)
            self.diaries.remove(diary)

        def validate_username(self, username):
            if username in self.diary == username:
                raise ValueError("Username is unavailable")

        def validate_password(self, password):
            if not re.search("^[0-9]\\d*", password):
                raise (ValueError, KeyboardInterrupt, "Password must contain at least one Uppercase character")


if __name__ == "__main__":
    mainDiary = MainDiary()
    mainDiary.main()



