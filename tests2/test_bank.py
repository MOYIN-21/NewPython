import unittest

from my_class.bank_account_app.account import Account
from my_class.bank import Bank


class Bank_test(unittest.TestCase):
    def setUp(self) -> None:
        self.bank = Bank("zenith")
        self.bank.register("ola", "mide", "0")

    def test_register(self):
        self.bank.register("ola","moyin", "0000")
        self.assertEqual(Account("1","ola moyin", "0000").get_account(),self.bank.find_account("1"))

    def test_that_bank_can_deposit(self):
        self.bank.register("ola", "mide", "0000")

        self.bank.deposit(5000, "1")
        new_account_balance = self.bank.check_balance("1", "0")
        self.assertEqual(5000, new_account_balance)

    def test_bank_can_not_deposit_negative_amount_into_a_given_account(self):
        self.bank.register("ola", "mide", "0")
        self.bank.deposit(2000, "1")

        new_account_balance = self.bank.check_balance("1", "0")

        self.assertEqual(2000, new_account_balance)

    def test_that_bank_can_withdraw(self):
        self.bank.register("ola", "mide", "0")
        self.bank.deposit(2000, "1")
        self.bank.with_draw("1", "1000", "0")
        current_balance = self.bank.check_balance("1", "0")
        self.assertEquals(1000, current_balance)

    def test_that_bank_can_transfer(self):
        self.bank.register("ola", "mide", "0")

        self.bank.deposit(5000, "1")
        self.bank.register("moyin", "mide", "0")
        self.assertEquals(
            self.bank.find_account("2").get_account_number().account("2", "ola mide", "0").get_account_number_balance)

        self.bank.transfer("0", "2", "1", "3000")

        self.assertEqual(3000, self.bank.check_balance("1", "0000"))

    def test_check_balance(self):
        self.bank.register("ola", "mide", "0")
        self.assertEqual(0, self.bank.check_balance("1", "0000"))

        self.bank.deposit(5000, "1")

        self.assertEqual(5000, self.bank.check_balance("1", "0000"))

    def test_to_withdraw_above_balance(self):
        self.bank.register("ola", "mide", "0")
        self.bank.deposit(5000, "1")
        current_balance = self.bank.check_balance("1", "0")
        self.assertEquals(5500, current_balance)
