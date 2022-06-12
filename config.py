import pathlib

PRICE_FILEPATH = pathlib.Path.cwd() / "prices.yml"
LOGGING_FILEPATH = pathlib.Path.cwd() / "logging.conf"
CART_DATA_FILEPATH = pathlib.Path.cwd() / "output/cart_data.json"
# mapping currency names to their respective symbols
# this information can also be retrieved from a database
CURRENCIES = {"euro": "€", "dollar": "$", "naira": "₦", "pound": "£"}
INITIAL_REF_NUMBER = 100
# this is the local currency name to be used across the shopping cart
LOCAL_CURRENCY = "euro"
