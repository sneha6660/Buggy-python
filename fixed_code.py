"""
fixed_code.py — Shopping Cart & Discount Module (Corrected Version)
Author: Sneha Kumari

This module resolves all 4 issues identified during the Cursor AI code review:
1. Replaced mutable default list with `None` sentinel.
2. Corrected bulk discount boundary check to `>= 3`.
3. Guarded against ZeroDivisionError by returning 0.0 for empty carts.
4. Standardized dictionary keys using a NamedTuple / typed data class.
"""

from typing import List, Optional, NamedTuple


class CartItem(NamedTuple):
    name: str
    price: float


def create_cart(initial_items: Optional[List[CartItem]] = None) -> List[CartItem]:
    """
    FIX 1: Safe list initialization.
    Uses `None` as default, creating a fresh list for every new cart.
    """
    if initial_items is None:
        return []
    return list(initial_items)


def add_item(cart: List[CartItem], name: str, price: float) -> List[CartItem]:
    """
    FIX 4: Typed CartItem avoids key-casing errors and validates price.
    """
    if price < 0:
        raise ValueError(f"Price cannot be negative: {price}")
    cart.append(CartItem(name=name, price=float(price)))
    return cart


def calculate_subtotal(cart: List[CartItem]) -> float:
    """Calculates sum of item prices in cart."""
    return round(sum(item.price for item in cart), 2)


def apply_volume_discount(cart: List[CartItem], subtotal: float) -> float:
    """
    FIX 2: Correct boundary condition.
    Orders with 3 or more items qualify for a 10% volume discount.
    """
    if len(cart) >= 3:  # CORRECT: >= 3 includes 3-item carts
        return round(subtotal * 0.90, 2)
    return round(subtotal, 2)


def calculate_average_price(cart: List[CartItem]) -> float:
    """
    FIX 3: Division-by-zero protection.
    Returns 0.0 cleanly when the cart contains no items.
    """
    if not cart:
        return 0.0
    return round(calculate_subtotal(cart) / len(cart), 2)


def generate_cart_summary(cart: List[CartItem]) -> dict:
    """Returns a full financial breakdown for the shopping cart."""
    subtotal = calculate_subtotal(cart)
    final_total = apply_volume_discount(cart, subtotal)
    discount_amount = round(subtotal - final_total, 2)
    avg_price = calculate_average_price(cart)

    return {
        "item_count": len(cart),
        "items": [item.name for item in cart],
        "subtotal": subtotal,
        "discount_amount": discount_amount,
        "final_total": final_total,
        "average_item_price": avg_price,
    }


def main():
    print("=" * 55)
    print("      FIXED SHOPPING CART & DISCOUNT SYSTEM")
    print("=" * 55)

    print("\n1. Testing Cart Isolation (Fix 1):")
    user1 = create_cart()
    add_item(user1, "Notebook", 50.0)
    user2 = create_cart()
    print(f"  User 1 Cart: {[i.name for i in user1]}")
    print(f"  User 2 Cart: {[i.name for i in user2]} (Properly empty!)")

    print("\n2. Testing 3-Item Volume Discount (Fix 2):")
    three_items = create_cart()
    add_item(three_items, "Pen", 10.0)
    add_item(three_items, "Book", 100.0)
    add_item(three_items, "Ruler", 20.0)
    summary_3 = generate_cart_summary(three_items)
    print(f"  Subtotal: Rs. {summary_3['subtotal']}")
    print(f"  10% Discount: Rs. {summary_3['discount_amount']}")
    print(f"  Final Total: Rs. {summary_3['final_total']}")

    print("\n3. Testing Empty Cart Average Protection (Fix 3):")
    empty = create_cart()
    summary_empty = generate_cart_summary(empty)
    print(f"  Empty cart average: Rs. {summary_empty['average_item_price']} (No crash!)")


if __name__ == "__main__":
    main()
