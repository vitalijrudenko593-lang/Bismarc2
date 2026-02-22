import logging

logging.basicConfig(level=logging.ERROR)

try:
    a = 10
    b = 0
    c = a / b
except Exception as error:
    logging.error(error)