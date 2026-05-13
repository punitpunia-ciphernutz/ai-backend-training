import time
from decorator import timer_logger


@timer_logger
def add(a, b):
    time.sleep(1)
    return a + b


@timer_logger
def multiply(a, b):
    time.sleep(2)
    return a * b