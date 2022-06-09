import pathlib

PRICE_FILEPATH = pathlib.Path.cwd() / "prices.yml"
LOGGING_FILEPATH = pathlib.Path.cwd() / "logging.conf"

# mapping currency names to their respective symbols
# this information can also be retrieved from a database
CURRENCIES = {"euro": "€", "dollar": "$", "naira": "₦", "pound": "£"}

# this is the local currency name to be used across the shopping cart
LOCAL_CURRENCY = "euro"
