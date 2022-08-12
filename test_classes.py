import unittest
from classes import *


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tv1 = Television()

    def tearDown(self) -> None:
        del self.tv1

    def test_init(self):
        assert self.tv1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'

    def test_power(self):
        self.tv1.power()
        assert self.tv1.__str__()[19:23] == 'True'  # add assertion here
        self.tv1.power()
        assert self.tv1.__str__()[19:24] == 'False'  # add assertion here

    def test_channel_up(self):
        self.tv1.channel_up()
        assert self.tv1.__str__()[36] == '0'  # add assertion here

        self.tv1.power()
        self.tv1.channel_up()
        assert self.tv1.__str__()[35] == '1'  # add assertion here
        self.tv1.channel_up()
        assert self.tv1.__str__()[35] == '2'  # add assertion here
        self.tv1.channel_up()
        assert self.tv1.__str__()[35] == '3'  # add assertion here
        self.tv1.channel_up()
        assert self.tv1.__str__()[35] == '0'  # add assertion here

    def test_channel_down(self):
        self.tv1.channel_down()
        assert self.tv1.__str__()[36] == '0'  # add assertion here

        self.tv1.power()
        self.tv1.channel_down()
        assert self.tv1.__str__()[35] == '3'  # add assertion here
        self.tv1.channel_down()
        assert self.tv1.__str__()[35] == '2'  # add assertion here

    def test_volume_up(self):
        self.tv1.volume_up()
        assert self.tv1.__str__()[48] == '0'  # add assertion here

        self.tv1.power()
        self.tv1.volume_up()
        assert self.tv1.__str__()[47] == '1'  # add assertion here
        self.tv1.volume_up()
        assert self.tv1.__str__()[47] == '2'  # add assertion here
        self.tv1.volume_up()
        assert self.tv1.__str__()[47] == '2'  # add assertion here

    def test_volume_down(self):
        self.tv1.volume_down()
        assert self.tv1.__str__()[48] == '0'  # add assertion here

        self.tv1.power()
        self.tv1.volume_down()
        assert self.tv1.__str__()[47] == '0'  # add assertion here
        self.tv1.volume_down()
        assert self.tv1.__str__()[47] == '0'  # add assertion here


if __name__ == '__main__':
    unittest.main()
