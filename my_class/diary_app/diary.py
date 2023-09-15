from Class_chinchin.exceptions import *
from my_class.diary_app.entry import *


class Diary:

    def __init__(self, username: str, password: str):
        self.__list_of_entries = []
        self.__is_locked: bool = False
        self.username: str = username
        self.__password: str = password
        self.entry = 0

    def unlock_diary(self, password: str):
        if self.__password != password:
            return WrongPinException
        else:
            return self.__is_locked == False

    def is_locked(self):
        return self.is_locked

    def lock_diary(self):
        self.__is_locked == True

    def create_entry( self, Id: str, title: str, body: str):
        entry = Entry(Id, title, body)
        self.__list_of_entries.append(entry)

    def generateId(self):
        return len(self.__list_of_entries) + 1

    def find_entry_by_id(self, id: int):
        for entry in self.__list_of_entries:
            if entry.get_id() == id:
                return entry
        raise entryNotFoundException("Entry could not be found")

    def delete_entry(self, id: int):
        entry = self.find_entry_by_id(id)
        self.__list_of_entries.remove(entry)

    def update_entry(self, id: int, title: str, body: str):
        entry = self.find_entry_by_id(id)
        entry.set_id(id)
        entry.set_title(title)
        entry.set_body(body)

    def get_diary_by_username(self):
        return self.username
