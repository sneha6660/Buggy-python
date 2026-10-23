"""
buggy_code.py — Shopping Cart & Discount Module (Buggy Version)
Author: Sneha Kumari

This module contains 4 deliberate, realistic bugs for educational debugging practice:
1. Mutable default argument (shared cart state across customers)
2. Off-by-one threshold error on volume discounts
3. ZeroDivisionError when cart is empty
4. KeyError from inconsistent dictionary casing
"""

def create_cart(initial_items=[]):
    """
    BUG 1: Mutable default argument!
    In Python, default lists are created once at definition time.
    Calling create_cart() multiple times shares the same list!
    """
    return initial_items


def add_item(cart, name, price):
    """
    BUG 4: Inconsistent dictionary key casing.
    Stores key as 'price', but other functions expect 'Price'.
    """
    cart.append({"name": name, "price": price})
    return cart


def calculate_subtotal(cart):
    """Calculates sum of item prices in cart."""
    total = 0.0
    for item in cart:
        # Might raise KeyError if key casing differs
        total += item.get("Price", item.get("price", 0.0))
    return total


def apply_volume_discount(cart, subtotal):
    """
    BUG 2: Off-by-one error.
    Policy: 'Orders with 3 or more items get 10% discount.'
    Buggy implementation uses `> 3`, excluding orders with exactly 3 items!
    """
    if len(cart) > 3:  # BUG: should be >= 3
        return subtotal * 0.90
    return subtotal


def calculate_average_price(cart):
    """
    BUG 3: ZeroDivisionError!
    If the cart is empty, len(cart) is 0.
    """
    subtotal = calculate_subtotal(cart)
    return subtotal / len(cart)  # BUG: crashes if len(cart) == 0


def main():
    print("=== DEMONSTRATING BUG 1: MUTABLE DEFAULT ARGUMENT ===")
    user1_cart = create_cart()
    add_item(user1_cart, "Notebook", 50.0)
    print("User 1 Cart:", [i["name"] for i in user1_cart])

    user2_cart = create_cart()
    print("User 2 Cart (Expected empty, but leaked from User 1!):", [i["name"] for i in user2_cart])

    print("\n=== DEMONSTRATING BUG 2: OFF-BY-ONE DISCOUNT ===")
    three_item_cart = [
        {"name": "Pen", "price": 10.0},
        {"name": "Book", "price": 100.0},
        {"name": "Ruler", "price": 20.0},
    ]
    subtotal = calculate_subtotal(three_item_cart)
    discounted = apply_volume_discount(three_item_cart, subtotal)
    print(f"3-item cart subtotal: {subtotal}")
    print(f"After discount (Expected 117.0 with 10% off, got): {discounted}")

    print("\n=== DEMONSTRATING BUG 3: DIVISION BY ZERO ===")
    empty_cart = []
    try:
        avg = calculate_average_price(empty_cart)
        print("Average price:", avg)
    except ZeroDivisionError as err:
        print(f"Crashed as expected: ZeroDivisionError ({err})")


if __name__ == "__main__":
    main()
