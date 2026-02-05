import pytest

@pytest.fixture
def valid_product():
    """Complete product with all fields."""
    return {
        "id": "prod_12345",
        "name": "Wireless Bluetooth Headphones",
        "in_stock": True
    }

@pytest.fixture
def minimal_product():
    """Product with only id and name (no in_stock field)."""
    return {
        "id": "prod_33333",
        "name": "USB-C Cable"
    }


def product_out_of_stock():
    """Product that is out of stock."""
    return {
        "id": "prod_11111",
        "name": "Limited Edition Sneakers",
        "in_stock": False
    }