import unittest

from converter import convert_currency


class TestCurrencyConverter(unittest.TestCase):

    def test_usd_to_inr(self):
        self.assertAlmostEqual(
            convert_currency(10, "USD", "INR"),
            830
        )

    def test_inr_to_usd(self):
        self.assertAlmostEqual(
            convert_currency(830, "INR", "USD"),
            10
        )

    def test_same_currency(self):
        self.assertAlmostEqual(
            convert_currency(100, "EUR", "EUR"),
            100
        )

    def test_invalid_amount(self):
        with self.assertRaises(ValueError):
            convert_currency(0, "USD", "INR")

    def test_invalid_currency(self):
        with self.assertRaises(ValueError):
            convert_currency(100, "ABC", "INR")


if __name__ == "__main__":
    unittest.main()