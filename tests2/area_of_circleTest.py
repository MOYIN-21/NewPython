import unittest
from math import pi

from my_class.area_of_circle import area


class Area_of_circle(unittest.TestCase):
    def test_area_function(self):
        self.assertAlmostEqual(area(1), pi)
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(2), pi * 2 ** 2)

    def test_values(self):
        self.assertRaises(ValueError, area, -1)
        self.assertRaises(ValueError, area, -5)

    def test_radius_type(self):
        self.assertRaises(TypeError, area, True)
        self.assertRaises(TypeError, area, 2 + 5j)



