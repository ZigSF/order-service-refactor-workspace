import unittest
from pricing import calculate_total_price

class TestPricing(unittest.TestCase):

    def test_basic_total(self):
        items = [{"price": 10, "quantity": 2}]
        result = calculate_total_price(items, 0.1)
        self.assertTrue(result > 0)

if __name__ == "__main__":
    unittest.main()
