import logging
import os.path


def my_logger(log_folder):
    """
     Initializes a logger that writes log messages to a file
     inside the provided log_folder. It creates the folder if
     it doesn't exist and configures the logger to store messages in a file named my_log.log.
    """
    os.makedirs(log_folder,exist_ok=True)

    log_file = os.path.join(log_folder, 'my_log.log')

    logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s::%(lineno)d::%(message)s")

    logger = logging.getLogger(__name__)
    logger.debug('Logger Initialized Successfully')

    return logger

if __name__ == "__main__":
    logger = my_logger('logs')
    logger.debug('Test Log Message')