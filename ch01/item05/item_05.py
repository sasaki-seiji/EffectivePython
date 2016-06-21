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
print("Example 1 : slice")
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('First four:', a[:4])
print('Last four: ', a[-4:])
print('Middle two:', a[3:-3])


# Example 2
print("\nExample 2 : omit start")
assert a[:5] == a[0:5]
print("a[:5]:", a[:5])


# Example 3
print("\nExample 3 : omit end")
assert a[5:] == a[5:len(a)]
print("a[5:]:", a[5:])

# Example 4
print("\nExample 4 : many slice examples")
print(a[:5])
print(a[:-1])
print(a[4:])
print(a[-3:])
print(a[2:5])
print(a[2:-1])
print(a[-3:-1])


# Example 5
print("\nExample 5 : many slice examples")
a[:]      # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print("a[:]:", a[:])
a[:5]     # ['a', 'b', 'c', 'd', 'e']
print("a[:5]:", a[:5])
a[:-1]    # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("a[:-1]:", a[:-1])
a[4:]     #                     ['e', 'f', 'g', 'h']
print("a[4:]:", a[4:])
a[-3:]    #                          ['f', 'g', 'h']
print("a[-3:]:", a[-3:])
a[2:5]    #           ['c', 'd', 'e']
print("a[2:5]:", a[2:5])
a[2:-1]   #           ['c', 'd', 'e', 'f', 'g']
print("a[2:-1]:", a[2:-1])
a[-3:-1]  #                          ['f', 'g']
print("a[-3:-1]", a[-3:-1])


# Example 6
print("\nExample 6 : out-of-range slice spec")
first_twenty_items = a[:20]
print("first_twenty_items", first_twenty_items)
last_twenty_items = a[-20:]
print("last_twenty_items", last_twenty_items)


# Example 7
print("\nExample 7 : out-of-range index")
try:
    a[20]
except:
    logging.exception('Expected')
else:
    assert False


# Example 8
print("\nExample 8 : slice makes copied list")
b = a[4:]
print('Before:   ', b)
b[1] = 99
print('After:    ', b)
print('No change:', a)


# Example 9
print("\nExample 9 : slice assign")
print('Before ', a)
a[2:7] = [99, 22, 14]
print('After  ', a)


# Example 10
print("\nExample 10 : x[:] makes copy")
b = a[:]
assert b == a and b is not a
print("b:", b, ", b is not a:", b is not a)

# Example 11
print("\nExample 11 : x[:] = y : replace list")
b = a
print('Before', a)
a[:] = [101, 102, 103]
assert a is b           # Still the same list object
print('After ', a)      # Now has different contents
