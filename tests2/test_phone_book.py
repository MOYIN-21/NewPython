from unittest import TestCase

from my_class.phone_book.phoneBook import phonebook


class Test(TestCase):
    my_phonebook = phonebook()
    my_phonebook.create_contact("Moyin", "Ola", "09026112098", "Ola@gmail.com")

    def test_create_contact(self):

        self.assertEqual(2, self.my_phonebook.count_contact())

    def test_contact_can_be_viewed(self):
        self.my_phonebook.create_contact("Moy", "Ola", "09026112098", "Ola@gmail.com")

        expected = """
       Contact Name: Moy Ola
       Contact Phone Number: 09026112098
       Contact Email-Address: Ola@gmail.com
       """
        self.assertEqual(expected,  self.my_phonebook.view_contact("Moy Ola"))

    def test_that_contact_can_be_edited(self):
        self.my_phonebook.edit_contact("Moyin Ola", "Ola", "mide", "070", "ple")
        expected = """
       Contact Name: Ola mide
       Contact Phone Number: 070
       Contact Email-Address: ple
       """
        self.assertEqual(expected, self.my_phonebook.view_contact("Ola mide"))

    def test_contact_can_be_deleted(self):
        self.my_phonebook.create_contact("Moy", "Ola", "09026112098", "Ola@gmail.com")
        self.my_phonebook.delete_contact("Moyin Ola")
        self.assertEqual(1, self.my_phonebook.count_contact())
