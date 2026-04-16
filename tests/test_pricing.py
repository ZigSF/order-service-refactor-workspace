import unittest
from pricing import calculate_total_price
from discounts import apply_discount


class TestPricing(unittest.TestCase):

    def test_basic_total(self):
        items = [{"price": 10, "quantity": 2}]
        result = calculate_total_price(items, 0.1)
        self.assertTrue(result > 0)

    def test_basic_total_exact_value(self):
        items = [{"price": 10, "quantity": 2}]
        result = calculate_total_price(items, 0.1)
        self.assertAlmostEqual(result, 22.0)

    def test_multiple_items(self):
        items = [
            {"price": 50, "quantity": 2},
            {"price": 25, "quantity": 1},
        ]
        result = calculate_total_price(items, 0.08)
        # subtotal = 100 + 25 = 125, tax = 125 * 0.08 = 10, total = 135
        self.assertAlmostEqual(result, 135.0)

    def test_empty_items(self):
        result = calculate_total_price([], 0.1)
        self.assertAlmostEqual(result, 0.0)

    def test_zero_tax_rate(self):
        items = [{"price": 15, "quantity": 3}]
        result = calculate_total_price(items, 0.0)
        self.assertAlmostEqual(result, 45.0)

    def test_zero_quantity(self):
        items = [{"price": 10, "quantity": 0}]
        result = calculate_total_price(items, 0.1)
        self.assertAlmostEqual(result, 0.0)

    def test_zero_price(self):
        items = [{"price": 0, "quantity": 5}]
        result = calculate_total_price(items, 0.1)
        self.assertAlmostEqual(result, 0.0)

    def test_single_item_no_tax(self):
        items = [{"price": 100, "quantity": 1}]
        result = calculate_total_price(items, 0.0)
        self.assertAlmostEqual(result, 100.0)


class TestDiscount(unittest.TestCase):

    def test_save10_returns_none(self):
        result = apply_discount(100.0, "SAVE10")
        self.assertIsNone(result)

    def test_save20_returns_none(self):
        result = apply_discount(100.0, "SAVE20")
        self.assertIsNone(result)

    def test_vip_returns_none(self):
        result = apply_discount(100.0, "VIP")
        self.assertIsNone(result)

    def test_unknown_code_returns_none(self):
        result = apply_discount(100.0, "UNKNOWN")
        self.assertIsNone(result)

    def test_none_code_returns_none(self):
        result = apply_discount(100.0, None)
        self.assertIsNone(result)

    def test_empty_string_code_returns_none(self):
        result = apply_discount(100.0, "")
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
