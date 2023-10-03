import unittest

from my_class.BankApp.account import Account


class AccountTest(unittest.TestCase):

    def setUp(self):
        self.account = Account("1", "Harry Nwa", "2345")

    def test_that_account_exists(self):
        self.assertTrue(self.account)

    def test_that_account_can_deposit(self):
        self.account.deposit(7000)
        self.assertEqual(7000, self.account.check_balance("2345"))

    def test_that_account_can_withdraw(self):
        self.account.deposit(7000)
        self.assertEqual(7000, self.account.check_balance("2345"))
        self.account.withdraw(5000, "2345")
        self.assertEqual(2000, self.account.check_balance("2345"))

    def test_that_account_can_change_pin(self):
        self.account.change_pin("2345", "5687")
        self.assertEqual(None, self.account.change_pin("2345",  "5687"))