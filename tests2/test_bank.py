import unittest

from my_class.BankApp.account import *
from my_class.BankApp.bank import *


class BankTest(unittest.TestCase):
    def setUp(self):
        self.bank = Bank("Tranxactrust")

    def test_that_bank_can_create_account(self):
        self.bank.register_bank_account("Harry", "Nwa", "2345")
        self.assertEqual(Account("1", "Harry Nwa", "2345").get_account(), self.bank.find_account("1").get_account())
        # self.assertEqual(Account(self.bank.generate_account_number(), "Harry Nwa", "2345").get_account(), self.bank.find_account("0").get_account())
        self.bank.register_bank_account("James", "Ikenna", "5432")
        self.assertEqual(Account("2", "James Ikenna", "5432").get_account(), self.bank.find_account("2").get_account())

    def test_that_bank_can_deposit(self):
        self.bank.register_bank_account("Harry", "Nwa", "2345")
        self.assertEqual(Account("1", "Harry Nwa", "2345").get_account(), self.bank.find_account("1").get_account())
        self.bank.deposit(10000, "1")
        self.assertEqual(10000, self.bank.check_balance("1", "2345"))
        self.bank.deposit(-10000, "1")
        self.assertEqual(10000, self.bank.check_balance("1", "2345"))

    def test_that_bank_can_withdraw(self):
        self.bank.register_bank_account("Harry", "Nwa", "2345")
        self.assertEqual(Account("1", "Harry Nwa", "2345").get_account(), self.bank.find_account("1").get_account())
        self.bank.deposit(10000, "1")
        self.assertEqual(10000, self.bank.check_balance("1", "2345"))
        self.bank.withdraw(15000, "1", "2345")
        self.assertEqual(10000, self.bank.check_balance("1", "2345"))

    def test_that_bank_can_transfer(self):
        self.bank.register_bank_account("Harry", "Nwa", "2345")
        self.assertEqual(Account("1", "Harry Nwa", "2345").get_account(), self.bank.find_account("1").get_account())
        self.bank.register_bank_account("James", "Ikenna", "5432")
        self.assertEqual(Account("2", "James Ikenna", "5432").get_account(), self.bank.find_account("2").get_account())
        self.bank.deposit(10000, "1")
        self.assertEqual(10000, self.bank.check_balance("1", "2345"))
        self.bank.transfer(5000, "1", "2", "2345")
        self.assertEqual(5000, self.bank.check_balance("1", "2345"))
        self.assertEqual(5000, self.bank.check_balance("2", "5432"))