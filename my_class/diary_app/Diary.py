
from my_class.diary_app.Entry import Entry


class Diary:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self.isLocked = False
        self.__entries = []

    def get_username(self):
        return self.username

    def validate_password(self, password):
        if self.__password != password:
            raise ValueError("Invalid password")

    def get_password(self, password):
        return self.validate_password(password)

    def unlock_diary(self, password):
        self.lock_diary()
        self.validate_password(password)
        self.isLocked = False

    def lock_diary(self):
        self.isLocked = True

    def is_locked(self):
        if self.isLocked:
            self.validate_password(self.__password)
            return False
        raise ValueError("Invalid password")

    def create_entry(self, title, body):
        entry = Entry(self.generate_entry_id(), title, body)
        self.__entries.append(entry)

    def generate_entry_id(self):
        return len(self.__entries) + 1

    def delete_entry(self, id):
        entry = self.find_entry_by_id(id)
        self.__entries.remove(entry)

    def find_entry_by_id(self, id):
        for entry in self.__entries:
            if entry.get_entry_id() == id:
                return entry

            raise ValueError("Entry ID not found")

    def update_entry(self, id, title, body):
        entry = self.find_entry_by_id(id)
        entry.set_title(title)
        entry.set_body(body)
        entry.set_id(id)