import unittest
from my_class.diary_app.Diary import *

class DiaryTest(unittest.TestCase):
    def setUp(self):
        self.diary = Diary("Username", "Password")

    def test_that_diary_exists(self):
        self.assertIsNotNone(self.diary)

    def test_that_diary_can_unlock(self):
        check = self.diary.lock_diary()
        confirm_password = self.diary.get_password("Password")
        self.assertEqual(check, confirm_password)

    def test_that_entry_can_be_created(self):
        check = self.diary.lock_diary()
        confirm_password = self.diary.get_password("Password")
        self.assertEqual(check, confirm_password)
        self.diary.create_entry("Clean Code", "Code with care")
        self.diary.find_entry_by_id(1)
        self.assertEqual("Clean Code", self.diary.find_entry_by_id(1).get_title())

    def test_that_entry_can_be_found_by_id(self):
        check = self.diary.lock_diary()
        confirm_password = self.diary.get_password("Password")
        self.assertEqual(check, confirm_password)
        self.diary.create_entry("The art of learning", "Learn daily. Practice often")
        self.assertEqual(1, Entry(1, "The art of learning", "Learn daily. Practice often").get_entry_id(), self.diary.find_entry_by_id(1))
        self.diary.create_entry("Understanding Programming", "Learn daily. Practice often")
        self.assertEqual(2, Entry(2,"Understanding Programming", "Learn daily. Practice often").get_entry_id(), self.diary.find_entry_by_id(2))

    def test_that_entry_can_be_deleted(self):
        check = self.diary.lock_diary()
        confirm_password = self.diary.get_password("Password")
        self.assertEqual(check, confirm_password)
        self.diary.create_entry("The art of learning", "Learn daily. Practice often")
        self.assertEqual("The art of learning", self.diary.find_entry_by_id(1).get_title())
        self.diary.create_entry("Understanding Programming", "Learn daily. Practice often")
        self.assertEqual("Understanding Programming", self.diary.find_entry_by_id(2).get_title())
        self.diary.create_entry("Religion is the Opium of the People", "The action and inaction of people's religiosity...")
        self.assertEqual("Religion is the Opium of the People", self.diary.find_entry_by_id(3).get_title())
        self.diary.delete_entry(1)
        self.assertRaises(ValueError, self.diary.find_entry_by_id, 1)

    def test_that_entry_can_be_updated(self):
        check = self.diary.lock_diary()
        confirm_password = self.diary.get_password("Password")
        self.assertEqual(check, confirm_password)
        self.diary.create_entry("Religion is the Opium of the People", "The action and inaction of people's religiosity...")
        self.diary.update_entry(1, "Religion is the Opium of the People", "The action and inaction of people's religiosity is not unconnected to the many unrealised dreams wrongly attributed to fate or destiny.")
        self.assertEqual("The action and inaction of people's religiosity is not unconnected to the many unrealised dreams wrongly attributed to fate or destiny.",
            self.diary.find_entry_by_id(1).get_body())


if __name__ == '__main__':
    unittest.main()