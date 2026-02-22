import os
import logging

def my_logger():
    """
    sets up a logger for the Amortization Table

    Returns:
        logger: The logger that can be used to log messages

    """

    folder_path = 'debt_repayment/files/logs/'
    os.makedirs(folder_path, exist_ok=True)

    log_file = os.path.join(folder_path, 'getting_out_of_debt.log')

    logger = logging.getLogger('AmortizationTable')
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s UTC - %(levelname)s - %(name)s - Line # %(lineno)d: %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger

def main():
    test_logger = my_logger()
    test_logger.debug('Test Debug (⌐■_■)')
    test_logger.info('Test info (⌐■_■)')
    test_logger.warning('Test Warning (⌐■_■)')
    test_logger.error('Test error(⌐■_■)')
    test_logger.critical('Test critical (⌐■_■)')


if __name__ == '__main__':
    main()