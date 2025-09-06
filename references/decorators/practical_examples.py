import time

#calculate time taken to run any function
def mytimer(func):
    start = time.time()
    def inner_func(*args, **kwargs):
        result = func(*args, **kwargs)
        stop = time.time()
        print(f"{func.__name__} ran in {stop-start} seconds")
        return result
    return inner_func

#used as logger for any function
def mylogger(func):
    import logging
    logging.basicConfig(filename=f"{func.__name__}.log", level=logging.INFO)
    def wrapper(*args, **kwargs):
        logging.info(f"Ran with args: {args}, and kw args: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@mytimer    #sleep_func = mytimer(sleep_func(sleep_time))
def sleep_func(sleep_time):
    print(f"sleeping for {sleep_time} seconds")
    time.sleep(sleep_time)
    print("Done with execution")

@mylogger   #display_info = mytimer(display_info(name,age))
def display_info(name,age):
    print(f"display_info function ran with arguments: {name} {age}")

# sleep_func(2) #calls decorated function wrapper inside timer

# display_info("pasupathi", '30') #calls decorated function wrapper inside mylogger
# display_info("thumbur", '30')


#Advanced
@mylogger 
@mytimer #display_info = mytimer(display_info(name,age))
def display_info(name,age):
    print(f"display_info function ran with arguments: {name} {age}")

#above code equal to 
# display_info = mylogger(mytimer(display_info))
display_info('temp', 100)