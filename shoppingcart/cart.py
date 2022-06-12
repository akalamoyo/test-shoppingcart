# -*- coding: utf-8 -*-
import logging.config
from typing import List

import yaml
import json
from config import (
    CURRENCIES,
    LOCAL_CURRENCY,
    LOGGING_FILEPATH,
    PRICE_FILEPATH,
    CART_DATA_FILEPATH,
    INITIAL_REF_NUMBER,
)

from . import base

logging.config.fileConfig(LOGGING_FILEPATH, disable_existing_loggers=False)
logger = logging.getLogger(__name__)


class ShoppingCart(base.ShoppingCart):
    def __init__(self):
        self._items = dict()
        self._currency = CURRENCIES[LOCAL_CURRENCY]
        # initialize cart_data to collect cart data
        self.cart_data = dict()
        self.cart_data.update({"cart_reference_number": INITIAL_REF_NUMBER})

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

    def print_receipt(self, write_to_file=True) -> List[str]:
        """
        Generate receipt, total_cost and quantity of item(s) in cart
        """

        item_lines = []
        total_cost = []
        total_quantity = []

        for item in self._items.items():
            if self._get_product_price(item[0]):
                total_quantity.append(item[1])
                price = self._get_product_price(item[0]) * item[1]
                total_cost.append(price)
                price_with_currency = "{}{:.2f}".format(self._currency, price)
                item_lines.append(
                    "{} - {} - {}".format(item[0], str(item[1]), price_with_currency)
                )

        self.cart_data.update(
            {
                "items": item_lines,
                "total_quantity": sum(total_quantity),
                "currency": self._currency,
                "total_cost": sum(total_cost),
            }
        )

        item_lines.append(
            "{} - {}{:.2f}".format("Total", self._currency, sum(total_cost))
        )

        logger.info("Cart checked out successfully")

        if write_to_file:
            self._write_cart_data_to_file()
        return item_lines

    def _get_product_price(self, product_code: str) -> float:
        """
        Get product price given a product code, returns nothing if product is not found
        """

        with open(PRICE_FILEPATH) as input_file:
            price_file = yaml.safe_load(input_file)

        product_code_with_price = {
            product["product_code"]: product["price"]
            for product in price_file["prices"]
        }
        return product_code_with_price.get(product_code, None)

    def _write_cart_data_to_file(self):
        """
        Assign reference number and write cart_data to json file.
        """

        with open(CART_DATA_FILEPATH) as outfile:
            cart_data_list = json.load(outfile)

        if len(cart_data_list) != 0:
            # get maximum reference number in cart history and add an increment for new cart
            max_reference_number = max(
                [cart_dict["cart_reference_number"] for cart_dict in cart_data_list]
            )
            self.cart_data.update({"cart_reference_number": max_reference_number + 1})
        cart_data_list.append(self.cart_data)

        with open(CART_DATA_FILEPATH, "w") as json_file:
            json.dump(cart_data_list, json_file, indent=4, separators=(",", ": "))
