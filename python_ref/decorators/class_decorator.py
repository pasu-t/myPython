#used as logger for any function
import logging
def mylogger(func):
    import logging
    logging.basicConfig(filename=f"{func.__name__}.log", level=logging.INFO)
    def wrapper(*args, **kwargs):
        logging.info(f"Ran with args: {args}, and kw args: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

class decorator_class():
    def __init__(self, original_func):
        self.original_func = original_func
        logging.basicConfig(filename=f"{self.original_func.__name__}.log", level=logging.INFO)

    def __call__(self, *args, **kwargs):
        logging.info(f"Ran with args: {args}, and kw args: {kwargs}")
        return self.original_func(*args, **kwargs)

# @mylogger
@decorator_class
def display_info(name,age):
    print(f"display_info function ran with arguments: {name} {age}")

display_info("thumbur",30)