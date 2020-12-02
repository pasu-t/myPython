import unittest
from circles import circle_area
from math import pi

class  TestCircleArea(unittest.TestCase):
    """docstring for  TestCircleArea"""
    def test_area(self):
        #when radius > 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(2.1), pi*(2.1**2))
        self.assertAlmostEqual(circle_area(0), 0)

    def test_values(self):
        #Make sure value errors are raised when necessary
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        #Make sure type errors are raised when necessary
        self.assertRaises(TypeError, circle_area, "abcd")
        self.assertRaises(TypeError, circle_area, 3+4j)
        self.assertRaises(TypeError, circle_area, True)


#run the commandto verify: python -m unittest test_circles or python -m unittest