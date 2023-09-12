class Tv:

    def __init__(self):
        self.__channel = 0
        self.__volume = 0
        self.__on = False

    def turn_on(self):
        self.__on = True

    def turn_off(self):
        self.__on = False

    def volume_up(self):
        if self.__volume < 100:
            self.__volume = self.__volume

    def volume_down(self):
        self.__volume = self.__volume

    def set_volume(self, volume):
        self.__volume = volume

    def get_volume_up(self) -> int:
        if self.__volume >= 100:
            return 100
        else:
            return self.__volume + 1

    def get_volume_down(self) -> int:
        if self.__volume <= 0:
            return 0
        else:
            return self.__volume - 1

    def set_channel(self, channel):
        self.__channel = channel

    def get_channel_up(self):
        if self.__channel >= 100:
            return 100
        else:
            return self.__channel + 1

    def channel_up(self):
        if self.__channel <= 100:
            self.__channel = self.__channel

    def channel_down(self):
        if self.__channel >= 0:
            self.__channel = self.__channel

    def get_channel_down(self):
        if self.__channel <= 0:
            return 0
        else:
            return self.__channel - 1




