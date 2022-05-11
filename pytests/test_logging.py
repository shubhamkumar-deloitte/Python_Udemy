import logging


def test_logging():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logs.log')  # file
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")  # defining the format of logs messages
    fileHandler.setFormatter(formatter)  # passing the format to filehandler and passing filehandler to logger
    logger.addHandler(fileHandler)  # filehandler object into it, what format and what file

    logger.setLevel(logging.DEBUG)  # level set to INFO, it will skip all debug logs
    # types of logs
    logger.debug("debug statement")
    logger.info("information messages")
    logger.warning("warning received")
    logger.error("Assertion failed")
    logging.critical("critical mishap")
