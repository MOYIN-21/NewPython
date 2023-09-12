import unittest
from my_class.television import *


class televisionTest(unittest.TestCase):
    def setup(self):
        self.samsung = Tv()

    # def test_tv_can_be_turn_on(self):
    #     self.samsung = Tv()
    #     self.turn_on(True)
    #     self.assertTrue()
    #
    # def test_tv_can_be_turn_off(self):
    #     self.samsung = Tv()
    #     self.turn_on()
    #     self.assertEqual()

    def test_volume_up(self):
        self.samsung = Tv()
        self.samsung.set_volume(9)
        self.samsung.volume_up()

        volume = self.samsung.get_volume_up()

        self.assertEqual(10, volume)

    def test_volume_cant_increase_above_100(self):
        self.samsung = Tv()
        self.samsung.set_volume(100)
        self.samsung.volume_up()

        volume = self.samsung.get_volume_up()

        self.assertEqual(100, volume)

    def test_volume_down(self):
        self.samsung = Tv()
        self.samsung.set_volume(9)
        self.samsung.volume_down()

        volume = self.samsung.get_volume_down()

        self.assertEqual(8, volume)

    def test_volume_cant_decrease_below_0(self):
        self.samsung = Tv()
        self.samsung.set_volume(0)
        self.samsung.volume_down()

        volume = self.samsung.get_volume_down()

        self.assertEqual(0, volume)

    def test_channel_up(self):
        self.samsung = Tv()
        self.samsung.set_channel(30)
        self.samsung.channel_up()

        channel = self.samsung.get_channel_up()

        self.assertEqual(31, channel)

    def test_channel_cant_increase_above_100(self):
        self.samsung = Tv()
        self.samsung.set_channel(100)
        self.samsung.channel_up()

        channel = self.samsung.get_channel_up()

        self.assertEqual(100, channel)

    def test_channel_down(self):
        self.samsung = Tv()
        self.samsung.set_channel(30)
        self.samsung.channel_down()

        channel = self.samsung.get_channel_down()

        self.assertEqual(29, channel)

    def test_channel_cant_decrease_below_0(self):
        self.samsung = Tv()
        self.samsung.set_channel(1)
        self.samsung.channel_down()

        channel = self.samsung.get_channel_down()

        self.assertEqual(0, channel)
