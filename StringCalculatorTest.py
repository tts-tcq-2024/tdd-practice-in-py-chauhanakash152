import unittest
from StringCalculator import add


class TestStringCalculator(unittest.TestCase):
    def test_empty_string_expect_zero(self):
        """Empty string returns 0"""
        self.assertEqual(add(""), 0)

    def test_single_number_expect_same_number(self):
        """Single number input returns the number itself"""
        self.assertEqual(add("1"), 1)

    def test_two_numbers_comma_separated_expect_sum(self):
        """Two numbers separated by a comma should return their sum"""
        self.assertEqual(add("1,2"), 3)

    def test_multiple_numbers_comma_separated_expect_sum(self):
        """Multiple numbers separated by commas should return their sum"""
        self.assertEqual(add("1,2,3,4"), 10)

    def test_newline_as_delimiter_expect_sum(self):
        """Handle new lines between numbers"""
        self.assertEqual(add("1\n2,3"), 6)

    def test_invalid_format_comma_newline_throws_error(self):
        """Incorrect format with newline after a comma throws an error"""
        with self.assertRaises(ValueError):
            add("1,\n")

    def test_custom_delimiter_multiple_numbers_expect_sum(self):
        """Custom delimiter with multiple numbers should return their sum"""
        self.assertEqual(add("//;\n1;2;3"), 6)

    def test_multiple_negatives_throws_exception(self):
        """Multiple negative numbers should throw an exception with all negatives""" # noqa
        with self.assertRaises(ValueError) as context:
            add("-1,-2,3")
        self.assertEqual(str(context.exception), "negatives not allowed: -1, -2") # noqa

    def test_numbers_greater_than_1000_ignored_in_sum(self):
        """Numbers greater than 1000 should be ignored in the sum"""
        self.assertEqual(add("2,1001"), 2)

    def test_numbers_equal_to_1000_included_in_sum(self):
        """Numbers equal to 1000 should be included in the sum"""
        self.assertEqual(add("2,1000"), 1002)

    def test_custom_delimiter_variable_length_expect_sum(self):
        """Custom delimiter of any length should return the correct sum"""
        self.assertEqual(add("//[###]\n4###5###6"), 15)


if __name__ == '__main__':
    unittest.main()
