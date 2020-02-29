import unittest

from my_functions import add_ten, subtract_ten
from my_functions import concatenate, r_paste


class TestMath(unittest.TestCase):

    def test_add_ten(self):
        x_positive = add_ten(5)
        x_negative = add_ten(-5)
        x_zero = add_ten(0)
        x_float = add_ten(1.5)

        # Ensure calculations are correct
        self.assertEqual(x_positive, 15)
        self.assertEqual(x_negative, 5)
        self.assertEqual(x_zero, 10)
        self.assertEqual(x_float, 11.5)

        # Ensure add_ten always returns float
        self.assertIsInstance(x_positive, float)
        self.assertIsInstance(x_negative, float)
        self.assertIsInstance(x_zero, float)
        self.assertIsInstance(x_float, float)

    def test_subtract_ten(self):
        x_positive = subtract_ten(5)
        x_negative = subtract_ten(-5)
        x_zero = subtract_ten(0)

        # Ensure calculations are correct
        self.assertEqual(x_positive, -5)
        self.assertEqual(x_negative, -15)
        self.assertEqual(x_zero, -10)


class TestStrings(unittest.TestCase):

    def test_concatenate(self):
        result = concatenate("Hello", "World")

        # Ensure concatenation works correctly (no space)
        self.assertEqual(result, "HelloWorld")

    def test_r_paste(self):
        result = r_paste("Hello", "World")

        # Ensure r_paste works correctly (includes space)
        self.assertEqual(result, "Hello World")


if __name__ == "__main__":
    unittest.main()
