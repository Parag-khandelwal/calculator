import unittest
from src.calculator import Calculator

calci = Calculator()

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        actual = calci.addition(1,2,3,4,5)
        expected = sum([1,2,3,4,5])
        self.assertEqual(actual, expected)

    def test_substraction(self):
        actual = calci.substraction(10, 5)
        expected = 5
        self.assertEqual(actual, expected)

    def test_product(self):
        actual = calci.product(10, 5)
        expected = 50
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
