import unittest
from discounts import apply_discount, DISCOUNT_RATES


class TestApplyDiscountSAVE10(unittest.TestCase):

    def test_save10_applies_10_percent_off(self):
        result = apply_discount(100, "SAVE10")
        self.assertEqual(result, 90.0)

    def test_save10_with_fractional_total(self):
        result = apply_discount(49.99, "SAVE10")
        self.assertEqual(result, 44.99)

    def test_save10_with_large_total(self):
        result = apply_discount(10000, "SAVE10")
        self.assertEqual(result, 9000.0)


class TestApplyDiscountSAVE20(unittest.TestCase):

    def test_save20_applies_20_percent_off(self):
        result = apply_discount(100, "SAVE20")
        self.assertEqual(result, 80.0)

    def test_save20_with_fractional_total(self):
        result = apply_discount(49.99, "SAVE20")
        self.assertEqual(result, 39.99)

    def test_save20_with_large_total(self):
        result = apply_discount(10000, "SAVE20")
        self.assertEqual(result, 8000.0)


class TestApplyDiscountVIP(unittest.TestCase):

    def test_vip_applies_30_percent_off(self):
        result = apply_discount(100, "VIP")
        self.assertEqual(result, 70.0)

    def test_vip_with_fractional_total(self):
        result = apply_discount(49.99, "VIP")
        self.assertEqual(result, 34.99)

    def test_vip_with_large_total(self):
        result = apply_discount(10000, "VIP")
        self.assertEqual(result, 7000.0)


class TestApplyDiscountEdgeCases(unittest.TestCase):

    def test_zero_total_returns_zero(self):
        for code in DISCOUNT_RATES:
            result = apply_discount(0, code)
            self.assertEqual(result, 0.0, f"Expected 0.0 for code {code}")

    def test_very_small_total(self):
        result = apply_discount(0.01, "SAVE10")
        self.assertEqual(result, 0.01)

    def test_negative_total_still_applies_discount(self):
        result = apply_discount(-100, "SAVE10")
        self.assertEqual(result, -90.0)

    def test_result_is_rounded_to_two_decimals(self):
        # 33.33 * 0.9 = 29.997 -> should round to 30.0
        result = apply_discount(33.33, "SAVE10")
        self.assertEqual(result, 30.0)

    def test_float_precision(self):
        # 19.99 * 0.8 = 15.992 -> should round to 15.99
        result = apply_discount(19.99, "SAVE20")
        self.assertEqual(result, 15.99)


class TestApplyDiscountInvalidCodes(unittest.TestCase):

    def test_none_code_returns_original_total(self):
        result = apply_discount(100, None)
        self.assertEqual(result, 100)

    def test_empty_string_code_returns_original_total(self):
        result = apply_discount(100, "")
        self.assertEqual(result, 100)

    def test_unknown_code_returns_original_total(self):
        result = apply_discount(100, "BOGUS")
        self.assertEqual(result, 100)

    def test_lowercase_code_is_not_recognized(self):
        result = apply_discount(100, "save10")
        self.assertEqual(result, 100)

    def test_code_with_extra_whitespace_is_not_recognized(self):
        result = apply_discount(100, " SAVE10 ")
        self.assertEqual(result, 100)

    def test_numeric_code_returns_original_total(self):
        result = apply_discount(100, 12345)
        self.assertEqual(result, 100)


class TestDiscountRatesConstant(unittest.TestCase):

    def test_all_expected_codes_present(self):
        self.assertIn("SAVE10", DISCOUNT_RATES)
        self.assertIn("SAVE20", DISCOUNT_RATES)
        self.assertIn("VIP", DISCOUNT_RATES)

    def test_discount_rate_values(self):
        self.assertAlmostEqual(DISCOUNT_RATES["SAVE10"], 0.10)
        self.assertAlmostEqual(DISCOUNT_RATES["SAVE20"], 0.20)
        self.assertAlmostEqual(DISCOUNT_RATES["VIP"], 0.30)


if __name__ == "__main__":
    unittest.main()
