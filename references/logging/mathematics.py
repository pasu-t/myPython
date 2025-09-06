import logging
import employee

# logging.basicConfig(filename="mathematics.log", level=logging.DEBUG, filemode='w',
    # format="%(asctime)s: %(levelname)s %(name)s - %(message)s")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s: %(levelname)s %(name)s - %(message)s")

file_handler = logging.FileHandler('mathematics.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        # logger.error('Tried division by zero')
        logger.exception('Tried division by zero')
    else:
        return result

num1 = 10
num2 = 0

add_result = add(num1,num2)
# logging.info('Add: {} + {} = {}'.format(num1,num2,add_result))
logger.debug('Add: {} + {} = {}'.format(num1,num2,add_result))
substract_result = substract(num1,num2)
# logging.info('Substract: {} + {} = {}'.format(num1,num2,substract_result))
logger.debug('Substract: {} + {} = {}'.format(num1,num2,substract_result))
multiply_result = multiply(num1,num2)
# logging.info('Multiply: {} + {} = {}'.format(num1,num2,multiply_result))
logger.debug('Multiply: {} + {} = {}'.format(num1,num2,multiply_result))
divide_result = divide(num1,num2)
# logging.info('Divide: {} + {} = {}'.format(num1,num2,divide_result))
logger.debug('Divide: {} + {} = {}'.format(num1,num2,divide_result))
