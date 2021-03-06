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
print('Example 1: stride')
a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = a[::2]
evens = a[1::2]
print(odds)
print(evens)


# Example 2
print('\nExample 2: reverse by stride=-1')
x = b'mongoose'
y = x[::-1]
print(y)


# Example 3
print("\nExample 3: reverse utf-8 by stride=-1")
try:
    w = '謝謝'
    x = w.encode('utf-8')
    y = x[::-1]
    z = y.decode('utf-8')
except:
    logging.exception('Expected')
else:
    assert False


# Example 4
print("\nExample 4: stride = 2, -2")
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(a)
print("a[::2]", a[::2])   # ['a', 'c', 'e', 'g']
print("a[::-2]", a[::-2])  # ['h', 'f', 'd', 'b']


# Example 5
print("\nExample 5: start, end, stride")
print("a[2::2]", a[2::2])     # ['c', 'e', 'g']
print("a[-2::-2]", a[-2::-2])   # ['g', 'e', 'c', 'a']
print("a[-2:2:-2]", a[-2:2:-2])  # ['g', 'e']
print("a[2:2:-2]", a[2:2:-2])   # []


# Example 6
print("\nExample 6: separate stride and slice")
b = a[::2]   # ['a', 'c', 'e', 'g']
c = b[1:-1]  # ['c', 'e']
print(a)
print(b)
print(c)
