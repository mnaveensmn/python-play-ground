import logging
import logging.config

# Load logging configuration from the file
logging.config.fileConfig('logging.conf')

# Create a logger
logger = logging.getLogger('exampleLogger')
print(__name__)
# Example usage
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
