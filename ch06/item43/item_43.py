#!/usr/bin/env python3

# Copyright 2014 Brett Slatkin, Pearson Education Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Preamble to mimick book environment
import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 1
print("Example 1 : with lock:")
from threading import Lock
lock = Lock()
with lock:
    print('Lock is held')


# Example 2
print("\nExample 2 : lock.acquire(); try: finally: lock.release()")
lock.acquire()
try:
    print('Lock is held')
finally:
    lock.release()


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
print("\nExample 5-6 : set debug_logging using contextmanager")
from contextlib import contextmanager
@contextmanager
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


# Example 7
print("\nExample 7 : with open() as")
with open('my_output.txt', 'w') as handle:
    handle.write('This is some data!')


# Example 8
print("\nExample 8-9 : with contextmanager as ...")
@contextmanager
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
print("\nExample 10 : contextmanager reset loglevel")
logger = logging.getLogger('my-log')
logger.debug('Debug will not print')
logger.error('Error will print')
