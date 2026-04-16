import unittest
from pricing import calculate_total_price


class TestCalculateTotalPriceEdgeCases(unittest.TestCase):
    """Edge case tests for calculate_total_price.

    The function computes:
        sum(item['price'] * item['quantity']) * (1 + tax_rate)

    It currently performs no input validation, so these tests
    document the expected behavior for boundary and unusual inputs.
    """

    # ── Zero quantity ────────────────────────────────────────────────

    def test_zero_quantity_single_item(self):
        items = [{"price": 10.0, "quantity": 0}]
        result = calculate_total_price(items, 0.1)
        self.assertEqual(result, 0.0)

    def test_zero_quantity_among_other_items(self):
        items = [
            {"price": 50.0, "quantity": 0},
            {"price": 25.0, "quantity": 2},
        ]
        result = calculate_total_price(items, 0.1)
        self.assertAlmostEqual(result, 55.0)  # 50.0 * (1 + 0.1)

    def test_all_items_zero_quantity(self):
        items = [
            {"price": 100.0, "quantity": 0},
            {"price": 200.0, "quantity": 0},
        ]
        result = calculate_total_price(items, 0.08)
        self.assertEqual(result, 0.0)

    # ── Negative price ───────────────────────────────────────────────

    def test_negative_price_single_item(self):
        items = [{"price": -10.0, "quantity": 2}]
        result = calculate_total_price(items, 0.1)
        self.assertAlmostEqual(result, -22.0)  # -20 * 1.1

    def test_negative_price_mixed_with_positive(self):
        """A negative-price item acts as a credit/refund line."""
        items = [
            {"price": 100.0, "quantity": 1},
            {"price": -20.0, "quantity": 1},
        ]
        result = calculate_total_price(items, 0.1)
        self.assertAlmostEqual(result, 88.0)  # 80 * 1.1

    def test_negative_price_exceeds_positive(self):
        """Net subtotal is negative when credits exceed charges."""
        items = [
            {"price": 10.0, "quantity": 1},
            {"price": -50.0, "quantity": 1},
        ]
        result = calculate_total_price(items, 0.1)
        self.assertAlmostEqual(result, -44.0)  # -40 * 1.1

    # ── Negative quantity ────────────────────────────────────────────

    def test_negative_quantity(self):
        items = [{"price": 10.0, "quantity": -3}]
        result = calculate_total_price(items, 0.1)
        self.assertAlmostEqual(result, -33.0)  # -30 * 1.1

    # ── Very large quantities ────────────────────────────────────────

    def test_very_large_quantity(self):
        items = [{"price": 9.99, "quantity": 1_000_000}]
        result = calculate_total_price(items, 0.08)
        expected = 9.99 * 1_000_000 * 1.08
        self.assertAlmostEqual(result, expected, places=2)

    def test_very_large_quantity_multiple_items(self):
        items = [
            {"price": 5.00, "quantity": 10_000_000},
            {"price": 1.50, "quantity": 10_000_000},
        ]
        result = calculate_total_price(items, 0.05)
        expected = (5.00 * 10_000_000 + 1.50 * 10_000_000) * 1.05
        self.assertAlmostEqual(result, expected, places=2)

    def test_extremely_large_quantity(self):
        """Ensure no overflow with Python's arbitrary-precision ints."""
        items = [{"price": 1, "quantity": 10**18}]
        result = calculate_total_price(items, 0.0)
        self.assertEqual(result, 10**18)

    # ── Zero price ───────────────────────────────────────────────────

    def test_zero_price(self):
        items = [{"price": 0.0, "quantity": 5}]
        result = calculate_total_price(items, 0.1)
        self.assertEqual(result, 0.0)

    def test_zero_price_and_zero_quantity(self):
        items = [{"price": 0.0, "quantity": 0}]
        result = calculate_total_price(items, 0.1)
        self.assertEqual(result, 0.0)

    # ── Empty items list ─────────────────────────────────────────────

    def test_empty_items_list(self):
        result = calculate_total_price([], 0.1)
        self.assertEqual(result, 0.0)

    # ── Tax rate edge cases ──────────────────────────────────────────

    def test_zero_tax_rate(self):
        items = [{"price": 100.0, "quantity": 1}]
        result = calculate_total_price(items, 0.0)
        self.assertAlmostEqual(result, 100.0)

    def test_negative_tax_rate(self):
        """A negative tax rate effectively acts as a subsidy."""
        items = [{"price": 100.0, "quantity": 1}]
        result = calculate_total_price(items, -0.05)
        self.assertAlmostEqual(result, 95.0)  # 100 * 0.95

    def test_100_percent_tax_rate(self):
        items = [{"price": 50.0, "quantity": 2}]
        result = calculate_total_price(items, 1.0)
        self.assertAlmostEqual(result, 200.0)  # 100 * 2.0

    # ── Floating-point precision ─────────────────────────────────────

    def test_floating_point_precision(self):
        """Prices like $19.99 should not produce wild rounding errors."""
        items = [{"price": 19.99, "quantity": 3}]
        result = calculate_total_price(items, 0.07)
        expected = 19.99 * 3 * 1.07  # 64.1679
        self.assertAlmostEqual(result, expected, places=2)

    def test_fractional_penny_prices(self):
        items = [{"price": 0.01, "quantity": 1}]
        result = calculate_total_price(items, 0.08)
        self.assertAlmostEqual(result, 0.0108, places=4)

    # ── Single item (minimal valid input) ────────────────────────────

    def test_single_item_basic(self):
        items = [{"price": 25.0, "quantity": 4}]
        result = calculate_total_price(items, 0.08)
        self.assertAlmostEqual(result, 108.0)  # 100 * 1.08


if __name__ == "__main__":
    unittest.main()
