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
print("Example 1-2,4 : decorator")
def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('%s(%r, %r) -> %r' %
              (func.__name__, args, kwargs, result))
        return result
    return wrapper


# Example 2
@trace
def fibonacci(n):
    """Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return (fibonacci(n - 2) + fibonacci(n - 1))


# 2016.07.03 comment out for re-definition
# Example 3
#def fibonacci(n):
#    """Return the n-th Fibonacci number"""
#    if n in (0, 1):
#        return n
#    return (fibonacci(n - 2) + fibonacci(n - 1))
#
#fibonacci = trace(fibonacci)


# Example 4
fibonacci(3)


# Example 5
print("\nExample 5 : print decorator")
print(fibonacci)

# Example 6
print("\nExample 6 : dumps decorator")
try:
    # Example of how pickle breaks
    import pickle
    
    def my_func():
        return 1
    
    # This will be okay
    print(pickle.dumps(my_func))
    
    @trace
    def my_func2():
        return 2
    
    # This will explode
    print(pickle.dumps(my_func2))
except:
    logging.exception('Expected')
else:
    assert False


""" 2016.07.03 comment out
# Example 7
help(fibonacci)
"""

# Example 8
print("\nExample 8-9 : functools.wraps")
from functools import wraps
# 2016.07.03 rename : trace -> trace2
def trace2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('%s(%r, %r) -> %r' %
              (func.__name__, args, kwargs, result))
        return result
    return wrapper

# 2016.07.03 rename : fibonacci -> fibonacci2
@trace2
def fibonacci2(n):
    """Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return (fibonacci2(n - 2) +
            fibonacci2(n - 1))


""" 2016.07.03 comment out
# Example 9
help(fibonacci)
"""
# 2016.07.03 add
print(fibonacci2)
