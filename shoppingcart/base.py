
from abc import ABC, abstractmethod
import typing


class ShoppingCart(ABC):

    @abstractmethod
    def add_item(self, product_code: str, quantity: int):
        pass

    @abstractmethod
    def print_receipt(self) -> typing.List[str]:
        pass

    @abstractmethod
    def remove_item(self, product_code: str, quantity: int):
        pass

    @abstractmethod
    def empty_cart(self):
        pass
