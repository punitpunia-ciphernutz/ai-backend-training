from services import add, multiply

print("Add Result:", add(2, 3))
print("Multiply Result:", multiply(4, 5))

# import time
# import logging

# # setup logging
# logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


# def timer_decorator(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()

#         result = func(*args, **kwargs)

#         end = time.time()
#         execution_time = round(end - start, 4)

#         # structured logging
#         logging.info({
#             "function": func.__name__,
#             "execution_time": execution_time,
#             "args": args,
#             "kwargs": kwargs,
#             "result": result
#         })

#         return result
#     return wrapper


# # Apply to multiple functions

# @timer_decorator
# def add(a, b):
#     time.sleep(1)   # simulate delay
#     return a + b


# @timer_decorator
# def multiply(a, b):
#     time.sleep(2)   # simulate delay
#     return a * b


# # Run functions
# print("Add Result:", add(2, 3))
# print("Multiply Result:", multiply(4, 5))