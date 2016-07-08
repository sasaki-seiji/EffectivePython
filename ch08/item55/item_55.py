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
print("Example 1-2 : print(x) is same as '%s' % x")
print('foo bar')


# Example 2
print('%s' % 'foo bar')


# Example 3
print("\nExample 3 : print 5 and '5'")
print(5)
print('5')


# Example 4
print("\nExample 4 : repr(embedded-object)")
a = '\x07'
print(repr(a))


# Example 5
print("\nExample 5 : eval(repr(a)) == a")
b = eval(repr(a))
assert a == b
print("eval(repr(a)) == a :", eval(repr(a)) == a)


# Example 6
print("\nExample 6-7 : repr(x) is same as '%r' % x")
print(repr(5))
print(repr('5'))


# Example 7
print('%r' % 5)
print('%r' % '5')


# Example 8
print("\nExample 8 : str(class-object)")
class OpaqueClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = OpaqueClass(1, 2)
print(obj)


# Example 9
print("\nExample 9-10 : define __repr__ method")
class BetterClass(object):
    def __init__(self, x, y):
        self.x = 1
        self.y = 2
    def __repr__(self):
        return 'BetterClass(%d, %d)' % (self.x, self.y)


# Example 10
obj = BetterClass(1, 2)
print(obj)


# Example 11
print("\nExample 11 : print instance-dictionary")
obj = OpaqueClass(4, 5)
print(obj.__dict__)
