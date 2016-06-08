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
print("Example 1 - return None when Zero Division")
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

assert divide(4, 2) == 2
print("divide(4, 2) returns ", divide(4, 2))
assert divide(0, 1) == 0
print("divide(0, 1) returns ", divide(0, 1))
assert divide(3, 6) == 0.5
print("divide(3, 6) returns ", divide(3, 6))
assert divide(1, 0) == None
print("divide(1, 0) returns ", divide(1, 0))


# Example 2
print("\nExample 2 - explicit comparison with None(1/0)")
x, y = 1, 0
result = divide(x, y)
if result is None:
    print('Invalid inputs')
else:
    print('Result is %.1f' % result)


# Example 3
print("\nExample 3 - implicit comparison(0/5)")
x, y = 0, 5
result = divide(x, y)
if not result:
    print('Invalid inputs')  # This is wrong!
else:
    assert False


# Example 4
print("\nExample 4 - returns touple(status/value)")
def divide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None


# Example 5
print("\nExample 5 - check status part(5/0)")
x, y = 5, 0
success, result = divide(x, y)
if not success:
    print('Invalid inputs')


# Example 6
print("\nExample 6 - ignore status, check value(5/0)")
x, y = 5, 0
_, result = divide(x, y)
if not result:
    print('Invalid inputs')  # This is right

print("\nExample 6 - ignore status, check value(0/5)")
x, y = 0, 5
_, result = divide(x, y)
if not result:
    print('Invalid inputs')  # This is wrong


# Example 7
print("\nExample 7 - raise exception")
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e


# Example 8
print("\nExample 8 - (5/2)")
x, y = 5, 2
try:
    result = divide(x, y)
except ValueError:
    print('Invalid inputs')
else:
    print('Result is %.1f' % result)
