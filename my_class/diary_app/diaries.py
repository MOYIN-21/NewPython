from my_class.diary_app.diary import *


class Diary:
    def __init__(self):
        self.__diaries_of_entry = []

    def find_by_username(self, username):
        for diary in self.__diaries_of_entry:
            if diary.get_diary_by_username() == username:
                return diary

    def can_delete(self, username, password):
        if self.find_by_username(username) is not None:
            self.__diaries_of_entry.remove(self.find_by_username(username))

    def add_diary_to_list(self, username, password):
        diary_adding = Diary(username, password)
        self.__diaries_of_entry.append(diary_adding)
