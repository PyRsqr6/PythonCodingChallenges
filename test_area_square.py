import unittest
from area_square import area_square

class TestAreaSquare(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area_square(5),25)
        self.assertAlmostEqual(area_square(10),100)
    def test_value(self):
        self.assertRaises(ValueError, area_square,-5)
    def test_type(self):
        self.assertRaises(TypeError, area_square, "square")
        self.assertRaises(TypeError, area_square, True)