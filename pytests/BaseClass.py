import inspect
import logging


class BaseClass:

    def getLogger(self):

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logs.log')  # file
        formatter = logging.Formatter(
            "%(asctime)s :%(levelname)s : %(name)s : %(message)s")  # defining the format of logs messages
        fileHandler.setFormatter(formatter)  # passing the format to filehandler and passing filahandler to logger
        logger.addHandler(fileHandler)  # filehandler object into it, what format and what file

        logger.setLevel(logging.DEBUG)  # level set to INFO, it will skip all debug logs

        return logger
