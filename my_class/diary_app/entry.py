
class Entry:
    def __init__(self, id, title, body):
        self.__id = id
        self.__title = title
        self.__body = body

    def get_id(self):
        return self.__id

    def set_id(self, user_id):
        self.__id = user_id

    def get_title(self):
        return self.__title

    def set_title(self, user_title):
        self.__title = user_title

    def get_body(self):
        return self.__body

    def set_body(self, user_body):
        self.__body = user_body

    def get_entry(self):
        return f'{self.__id} {self.__title} {self.__body}'
