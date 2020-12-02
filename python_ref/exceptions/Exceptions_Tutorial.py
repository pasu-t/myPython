#common exceptions
import math
SyntaxError
ZeroDivisionError
TypeError #1 + 2 +"abcd"
ValueError #math.sqrt(-1) when type is valid but value cannot be handled, ValueError exception will be raised
FileNotFoundError
ModuleNotFoundError
IndexError
KeyError

try:
    pass #<code>
except:
    pass # run if exception occurs
else:
    pass #run if try block succeeds
finally:
    pass


#sample program
import logging
import time

logging.basicConfig(filename="C:\\Workspace\\myPython\\python_ref\\exceptions\\file.log", level=logging.DEBUG)
logger = logging.getLogger()

def read_file_timed(path):

    start_time = time.time()
    try:
        f = open(path, "rb")
        data = f.read()
        return data
    except FileNotFoundError as err:
        logger.error(err)
        raise
    else:
        f.close()
    finally:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info("time required for {file} = {time} ".format(file=path,time=dt))

read_file_timed("C:\\Users\\pasup\\Downloads\\Tamasha (2015) Hindi\\Tamasha (2015) Hindi - 720p BluRay.mkv")
# read_file_timed("C:\\Users\\pasup\\Downloads\\Tamasha (2015) Hindi\\Tamasha.mkv")
# read_file_timed("C:\\Users\\pasup\\Downloads\\Tamasha (2015) Hindi\\If you like My Work.txt")
