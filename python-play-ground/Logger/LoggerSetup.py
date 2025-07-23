import logging
import logging.config


def setup_logger():
    logging.config.fileConfig('logging2.conf')
    test_logger()

def test_logger():
    logger = logging.getLogger(__name__)
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')

if __name__ == '__main__':
    setup_logger()
    exit()