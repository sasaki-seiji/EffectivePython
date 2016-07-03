
# Preamble to mimick book environment
import logging
from pprint import pprint
from sys import stdout as STDOUT

class MyContextManager:
    def __init__(self, it):
        self.it = it
        
    def __enter__(self):
        return next(self.it)
    
    def __exit__(self, exc_type, exc_value, traceback):
        try:
            next(self.it)
        except StopIteration:
            pass

        
def mycontextmanager(func):
    def wrapper(*args, **kwargs):
        it = func(*args, **kwargs)
        return MyContextManager(it)
    
    return wrapper

# Example 3
print("\nExample 3-4 : logging sample")
import logging
logging.getLogger().setLevel(logging.WARNING)
def my_function():
    logging.debug('Some debug data')
    logging.error('Error log here')
    logging.debug('More debug data')


# Example 4
my_function()


# Example 5
print("\nExample 5-6 : set debug_logging using mycontextmanager")
#from contextlib import contextmanager
@mycontextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)


# Example 6
with debug_logging(logging.DEBUG):
    print('Inside:')
    my_function()
print('After:')
my_function()


# Example 8
print("\nExample 8-9 : with mycontextmanager as ...")
@mycontextmanager
def log_level(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)


# Example 9
with log_level(logging.DEBUG, 'my-log') as logger:
    logger.debug('This is my message!')
    logging.debug('This will not print')


# Example 10
print("\nExample 10 : mycontextmanager reset loglevel")
logger = logging.getLogger('my-log')
logger.debug('Debug will not print')
logger.error('Error will print')
