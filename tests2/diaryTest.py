import unittest

from Class_chinchin.exceptions import AccountNotFoundException
from my_class.diary_app.entry import *
from my_class.diary_app.diary import *


class InvalidIdException:
    pass


class TestDiaryFunction(unittest.TestCase):

    def setUp(self):
        username = "Username"
        password = "password"
        self.diary = Diary(username, password)

    def test_that_diary_exist(self):
        self.assertTrue(self.diary)

    def test_that_diary_is_locked(self):
        self.diary.lock_diary()
        self.assertTrue(self.diary.is_locked())

    def test_that_diary_is_unlocked(self):
        self.diary.lock_diary()
        unlock_diary("1234")

    def test_that_entry_can_be_created(self):
        self.diary.create_entry(1, "school days", "are memories")
        self.assertEqual("school days", self.diary.find_entry_by_id(1).get_title())

    def test_that_entry_can_be_deleted(self):
        self.diary.create_entry(1, "crazy things", "are happenings", )
        self.diary.delete_entry(1)
        self.assertRaises(entryNotFoundException, self.diary.find_entry_by_id, 1)

    def test_that_diary_can_be_updated(self):
        self.diary.create_entry(1, "code girl", "you too good")
        self.diary.update_entry(1, "while alive", "code")
        self.assertEqual(Entry(1, "while alive", "code").get_entry(), self.diary.find_entry_by_id(1).get_entry())


if __name__ == "__main__":
    unittest()
