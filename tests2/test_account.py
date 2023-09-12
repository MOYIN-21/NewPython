import unittest

from my_class.bank_account_app.account import Account


class accountTest(unittest.TestCase):
    def setUp(self):
        self.accounts = Account('2415109039', "ola", 0000)

    def test_deposit(self):
        self.accounts = Account('2415109039', "ola", 0000)
        self.accounts.deposit(5000)
        check = self.accounts.check_balance(0000)
        self.assertEqual(5000, check)

    def test_account_can_deposit(self):
        self.accounts.deposit(5000)
        self.assertEqual(5000, self.accounts.check_balance(0000))

    def test_account_can_not_deposit_negative_amount(self):
        self.accounts.deposit(5000)
        self.assertEqual(5000, self.accounts.check_balance(0000))

    def test_deposit_money_balance_increase(self):
        self.accounts.deposit(3000)
        self.accounts.deposit(2000)
        self.accounts.deposit(5000)
        self.assertEqual(10000, self.accounts.check_balance(0000))

    def test_account_can_withdraw(self):
        self.accounts.deposit(4000)
        self.accounts.withdraw(1000, 0000)
        self.assertEqual(3000, self.accounts.check_balance(0000))

    def test_account_cannot_withdraw_above_balance(self):
        self.accounts.deposit(4000)
        self.accounts.withdraw(3000, 0000)
        self.assertEqual(1000, self.accounts.check_balance(0000))

    def test_account_cannot_withdraw_with_wrong_pin(self):
        self.accounts.deposit(4000)
        self.accounts.withdraw(1000, 0000)
        self.assertEqual(3000, self.accounts.check_balance(0000))
