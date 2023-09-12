import unittest

from self import self

from my_class.tic_tac_toe.board import Board


class test_myTest(unittest.TestCase):
    self.board = Board("ola")

    def test_register_player(self):
        self.register_player("ola")
        self.assertEquals("ola", 1)
        self.test_register_player("player")
        self.assertEquals("player", 2)



