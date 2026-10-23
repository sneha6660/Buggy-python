"""
test_suite.py — Automated Unit Tests for Bug Fixing Project
Author: Sneha Kumari

Runs automated assertions verifying that:
1. Mutable defaults are isolated.
2. 3-item carts receive exactly 10% volume discount.
3. Empty carts do not raise ZeroDivisionError.
4. Prices and subtotals compute accurately.
"""

import unittest
import fixed_code


class TestFixedShoppingCart(unittest.TestCase):

    def test_cart_isolation_no_mutable_default_leak(self):
        """Verify that multiple carts do not share the default list."""
        cart1 = fixed_code.create_cart()
        fixed_code.add_item(cart1, "Item A", 25.0)

        cart2 = fixed_code.create_cart()
        self.assertEqual(len(cart2), 0, "Cart 2 should be completely empty and independent!")
        self.assertEqual(len(cart1), 1, "Cart 1 should retain its 1 item.")

    def test_volume_discount_threshold_boundary(self):
        """Verify 2-item orders get 0% and 3-item orders get 10% discount."""
        # 2 items: 10 + 20 = 30 -> No discount
        cart_2 = fixed_code.create_cart()
        fixed_code.add_item(cart_2, "Pen", 10.0)
        fixed_code.add_item(cart_2, "Pencil", 20.0)
        subtotal_2 = fixed_code.calculate_subtotal(cart_2)
        total_2 = fixed_code.apply_volume_discount(cart_2, subtotal_2)
        self.assertEqual(total_2, 30.0, "2 items should not receive volume discount.")

        # 3 items: 10 + 20 + 70 = 100 -> 10% off = 90.0
        cart_3 = fixed_code.create_cart()
        fixed_code.add_item(cart_3, "Pen", 10.0)
        fixed_code.add_item(cart_3, "Pencil", 20.0)
        fixed_code.add_item(cart_3, "Notebook", 70.0)
        subtotal_3 = fixed_code.calculate_subtotal(cart_3)
        total_3 = fixed_code.apply_volume_discount(cart_3, subtotal_3)
        self.assertEqual(total_3, 90.0, "3 items MUST receive 10% volume discount!")

    def test_empty_cart_zero_division_guard(self):
        """Verify average calculation on empty cart returns 0.0 without exception."""
        empty_cart = fixed_code.create_cart()
        avg = fixed_code.calculate_average_price(empty_cart)
        self.assertEqual(avg, 0.0, "Empty cart average must safely return 0.0.")

    def test_full_summary_calculation(self):
        """Verify complete summary breakdown."""
        cart = fixed_code.create_cart()
        fixed_code.add_item(cart, "Desk Mat", 200.0)
        fixed_code.add_item(cart, "Mousepad", 100.0)
        fixed_code.add_item(cart, "Cable", 100.0)
        # Subtotal: 400.0, 10% off: 360.0, avg: 133.33

        summary = fixed_code.generate_cart_summary(cart)
        self.assertEqual(summary["subtotal"], 400.0)
        self.assertEqual(summary["discount_amount"], 40.0)
        self.assertEqual(summary["final_total"], 360.0)
        self.assertEqual(summary["average_item_price"], 133.33)
        self.assertEqual(summary["item_count"], 3)


def run_tests():
    print("=" * 55)
    print("  RUNNING UNIT TESTS FOR BUG FIXING (CURSOR AI) PROJECT")
    print("=" * 55)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFixedShoppingCart)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("\n>>> ALL 4 TEST CASES PASSED SUCCESSFULLY!")
    else:
        print("\n>>> SOME TESTS FAILED.")
    return result.wasSuccessful()


if __name__ == "__main__":
    run_tests()
