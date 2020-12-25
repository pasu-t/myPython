
#closre: Even after the outer function is executed, its paramters are still available to inner function when we call them
import logging

logging.basicConfig(filename="math.log", level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info(f"Running {func} with arguments:{args}")
        print(func(*args))
    return log_func

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

add_logger = logger(add) #outer funtion executed. It has add function as parameter
sub_logger = logger(sub)

add_logger(2,8) #inner function executed by using add function passed by outer function (this is called closure)
sub_logger(10,5)
