import re

from my_class.diary_app import Diary


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
