import time


class Entry:
    id = 0
    time.localtime()

    def __init__(self, id, title, body):
        self.__title = title
        self.__body = body
        self.__id = id
        self.__date = time.localtime()

    def set_id(self, id):
            self.__id = id

    def get_entry_id(self):
        return self.__id

    def get_diary_info(self):
        return self.__title + " " + self.__body

    def get_diary_infos(self):
        return str(self.__id) + " " + self.__title + " " + self.__body

    def get_body(self):
        return self.__body

    def set_body(self, body):
        self.__body = body

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title