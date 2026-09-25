
# def add(p,q):
#     return p+q

# def sub(p,q):
#     return p-q

# def multiply(p,q):
#     return p*q

# def divide(p,q):
#     if q==0:
#         raise ValueError("we can't divide with zero")
#     return p/q

import logging

import os

LOG_DIR = "loggings"
LOG_FILE_NAME = "app.log"

os.makedirs(LOG_DIR, exist_ok=True)

log_path = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename=log_path, level=logging.INFO, format = "[ %(asctime)s] %(name)s - %(levelname)s - %(message)s",force=True)


def add(a,b):
    result=a+b
    logging.info(f"Adding {a} + {b}")
    return result

def subtract(a, b):
    result = a - b
    logging.info(f"Subtracting {a} - {b}")
    return result

def multiply(a, b):
    result = a * b
    logging.info(f"Multiplying {a} * {b}")
    return result

def divide(a, b):
    try:
        result = a / b
        logging.debug(f"Dividing {a} / {b}")
        return result
    except ZeroDivisionError:
        logging.error("Division by zero error")
        return None

