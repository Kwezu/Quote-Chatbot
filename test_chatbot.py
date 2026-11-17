# Tests for the quote logic in chatbot.py.
# None of these call input() or print(), so they run without a customer.
# Run them with: python3 -m pytest
from chatbot import calculate_total, add_service, build_receipt


# ===== calculate_total() =====

def test_total_of_empty_cart_is_zero():
    """An empty cart should total 0, not crash or return None."""
    assert calculate_total([]) == 0


def test_total_adds_all_prices():
    """Two services should add up: 4500 + 1800 = 6300."""
    cart = [
        {"service_name": "Screen Replacement", "price": 4500},
        {"service_name": "Battery Replacement", "price": 1800},
    ]
    assert calculate_total(cart) == 6300


# ===== add_service() =====

def test_add_service_adds_new_service():
    """A new service goes into the cart and add_service returns True."""
    cart = []
    assert add_service(cart, "Screen Replacement", 4500) is True
    assert len(cart) == 1


def test_add_service_rejects_duplicate():
    """The same service twice is refused: returns False, cart stays at one item."""
    cart = []
    add_service(cart, "Screen Replacement", 4500)
    assert add_service(cart, "Screen Replacement", 4500) is False
    assert len(cart) == 1


# ===== build_receipt() =====

def test_receipt_contains_customer_model_service_and_total():
    """The receipt text should include the customer, MacBook, service and total."""
    user = {"name": "Kwezu", "surname": "Lebisi"}
    cart = [{"service_name": "Screen Replacement", "price": 4500}]
    receipt = build_receipt(user, "MacBook Air 13-inch (2020, M1)", cart, 4500)
    assert "Kwezu Lebisi" in receipt
    assert "MacBook Air 13-inch (2020, M1)" in receipt
    assert "Screen Replacement: R4500" in receipt
    assert "Total Cost: R4500" in receipt