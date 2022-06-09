import pytest

from shoppingcart.cart import ShoppingCart


@pytest.fixture(scope="function")
def cart():
    return ShoppingCart()