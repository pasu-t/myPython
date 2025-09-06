
#logging allows status messages to a file
#Purpose: Records progress and problems
#Levels NOTSET-0, DEBUG-10, INFO-20, WARNING-30, ERROR-40, CRITICAL-50

import logging

LOG_FORMAT = "%(asctime)s %(levelname)s - %(message)s"
logging.basicConfig(filename="lumberjack.log", level=logging.DEBUG, format=LOG_FORMAT, filemode='w')
logger = logging.getLogger()

logger.info("Our first message")
logger.debug("Our debug message")
logger.warning("Our warning message")
logger.error("Our error message")
logger.critical("Our critical message")