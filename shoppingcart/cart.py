import logging.config
from typing import List

import yaml

from config import CURRENCIES, LOCAL_CURRENCY, LOGGING_FILEPATH, PRICE_FILEPATH

from . import base

logging.config.fileConfig(LOGGING_FILEPATH, disable_existing_loggers=False)
logger = logging.getLogger(__name__)


class ShoppingCart(base.ShoppingCart):
    def __init__(self):
        self._items = dict()
        self._currency = CURRENCIES[LOCAL_CURRENCY]
        # initialize cart_data to collect cart data
        self.cart_data = dict()

    def add_item(self, product_code: str, quantity: int):
        """
        Add item(s) to cart
        """
        if product_code not in self._items:
            self._items[product_code] = quantity
        else:
            increment_q = self._items[product_code]
            self._items[product_code] = increment_q + quantity

    def remove_item(self, product_code: str, quantity: int):
        """
        Remove item(s) from cart
        """
        if quantity >= self._items[product_code]:
            self._items.pop(product_code)
        else:
            decrement_q = self._items[product_code]
            self._items[product_code] = decrement_q - quantity

    def empty_cart(self):
        """
        Empty cart, delete all items at once
        """
        self._items = dict()

    def print_receipt(self) -> List[str]:
        """
        Generate receipt of item(s) in cart
        """
        item_lines = []
        total = []
        for item in self._items.items():
            if self._get_product_price(item[0]):
                price = self._get_product_price(item[0]) * item[1]
                total.append(price)
                price_with_currency = "{}{:.2f}".format(self._currency, price)
                item_lines.append(
                    "{} - {} - {}".format(item[0], str(item[1]), price_with_currency)
                )
        item_lines.append("{} - {}{:.2f}".format("Total", self._currency, sum(total)))
        self.cart_data.update({"items": item_lines})
        logger.info("Cart checked out successfully")
        return item_lines

    def _get_product_price(self, product_code: str) -> float:
        """
        Get product price given a product code, returns nothing if product is not found
        """
        with open(PRICE_FILEPATH) as f:
            price_file = yaml.safe_load(f)

        product_code_with_price = {
            product["product_code"]: product["price"]
            for product in price_file["prices"]
        }
        return product_code_with_price.get(product_code, None)


a = ShoppingCart()
a.print_receipt()
