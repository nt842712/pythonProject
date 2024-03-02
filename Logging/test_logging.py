import logging


def test_logging():
    logger = logging.getLogger(__name__)
    filehandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)  #fileHandler object

    logger.setLevel(logging.DEBUG)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is warning")
    logger.error("A major error has happened")
    logger.critical("Critical error")


