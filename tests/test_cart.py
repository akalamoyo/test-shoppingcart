def test_add_item(cart):
    """
    Test addition of single item to cart
    """
    cart.add_item("apple", 1)

    assert cart._items == {"apple": 1}


def test_add_item_multiple_times(cart):
    """
    Test addition of same item multiple times to cart
    """
    cart.add_item("kiwi", 1)
    cart.add_item("kiwi", 1)

    assert cart._items == {"kiwi": 2}


def test_add_item_with_multiple_quantity(cart):
    """
    Test addition of single item with multiple quantities to cart
    """
    cart.add_item("apple", 2)

    assert cart._items == {"apple": 2}


def test_add_different_items(cart):
    """
    Test addition of different items to cart
    """
    cart.add_item("banana", 1)
    cart.add_item("kiwi", 1)

    assert cart._items == {"banana": 1, "kiwi": 1}


def test_add_different_items_multiple_quantities(cart):
    """
    Test addition of different items with multiple quantities to cart
    """
    cart.add_item("banana", 2)
    cart.add_item("kiwi", 3)

    assert cart._items == {"banana": 2, "kiwi": 3}


def test_remove_item(cart):
    """
    Test removal of single quantity of an item
    """
    cart._items = {"apple": 2}
    cart.remove_item("apple", 1)

    assert cart._items == {"apple": 1}


def test_remove_item_with_multiple_quantity(cart):
    """
    Test removal of multiples quantities of an item
    """
    cart._items = {"apple": 5}
    cart.remove_item("apple", 3)

    assert cart._items == {"apple": 2}


def test_remove_different_items(cart):
    """
    Test removal of single quantity of a different items
    """
    cart._items = {"apple": 2, "kiwi": 3}
    cart.remove_item("apple", 1)
    cart.remove_item("kiwi", 1)

    assert cart._items == {"apple": 1, "kiwi": 2}


def test_remove_different_items_multiple_quantities(cart):
    """
    Test removal of multiple quantities of a different items
    """
    cart._items = {"apple": 2, "kiwi": 3}
    cart.remove_item("apple", 2)
    cart.remove_item("kiwi", 2)

    assert cart._items == {"kiwi": 1}


def test_empty_cart(cart):
    """
    Test emptying of cart
    """
    cart._items = {"kiwi": 1, "apple": 2}
    cart.empty_cart()

    assert cart._items == dict()


def test_print_receipt(cart):
    """
    Test printing of receipt of items in cart
    """
    cart._items = {"apple": 2, "kiwi": 3}
    receipt = cart.print_receipt()

    assert receipt[0] == "apple - 2 - €2.00"
    assert receipt[1] == "kiwi - 3 - €9.00"
    assert receipt[2] == "Total - €11.00"
