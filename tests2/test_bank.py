import unittest
from Class_chinchin.exceptions import*
from my_class.bank_account_app.account import Account
from my_class.bank_account_app.bank import Bank


class Bank_test(unittest.TestCase):
    def setUp(self) -> None:
        self.bank = Bank("zenith")
        self.bank.register("ola", "mide", "0000")

    def test_register(self):
        self.bank.register("olu","moyin", "0000")
        self.assertEqual(2,self.bank.number_of_account())

    def test_that_bank_can_deposit(self):
        self.bank.deposit("1", 5000)
        new_account_balance = self.bank.check_balance("1", "0000")
        self.assertEqual(5000, new_account_balance)

    def test_that_bank_can_withdraw(self):

        self.bank.deposit("1",2000)
        self.bank.with_draw("1", 1000, "0000")
        current_balance = self.bank.check_balance("1", "0000")
        self.assertEquals(1000, current_balance)

    def test_that_bank_can_transfer(self):

        self.bank.deposit("1", 5000)
        self.bank.register("moyin", "mide", "0000")
        self.bank.transfer("1", 3000, "2", "0000")

        self.assertEqual(3000, self.bank.check_balance("2", "0000"))

    def test_check_balance(self):
        self.bank.deposit("1", 1000)
        actual = self.bank.check_balance("1", "0000")
        self.assertEqual(1000, actual)

    def test_to_withdraw_above_balance(self):
        self.bank.deposit("1", 8000)
        self.bank.with_draw("1", 4000, "0000")
        balance = self.bank.check_balance("1", "0000")
        self.assertEquals(4000, balance)
