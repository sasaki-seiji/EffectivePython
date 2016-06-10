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
def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


# Example 2
print("Example 1-2 : iterate twice - normalize(list)")
visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)


# Example 3
path = 'my_numbers.txt'
with open(path, 'w') as f:
    for i in (15, 35, 80):
        f.write('%d\n' % i)

def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


# Example 4
print("\nExample 3-4 : normalize(iterator)")
it = read_visits('my_numbers.txt')
percentages = normalize(it)
print(percentages)


# Example 5
print("\nExample 5 : list(iterator) twice")
it = read_visits('my_numbers.txt')
print(list(it))
print(list(it))  # Already exhausted


# Example 6
def normalize_copy(numbers):
    numbers = list(numbers)  # Copy the iterator
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


# Example 7
print("\nExample 6-7 : normalize_copy(iterator)")
it = read_visits('my_numbers.txt')
percentages = normalize_copy(it)
print(percentages)


# Example 8
def normalize_func(get_iter):
    total = sum(get_iter())   # New iterator
    result = []
    for value in get_iter():  # New iterator
        percent = 100 * value / total
        result.append(percent)
    return result


# Example 9
print("\nExample 8-9 : normalize_func(lambda)")
percentages = normalize_func(lambda: read_visits(path))
print(percentages)


# Example 10
class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


# Example 11
print("\nExample 10-11 : normalize(specific-container)")
visits = ReadVisits(path)
percentages = normalize(visits)
print(percentages)


# Example 12
def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):  # An iterator -- bad!
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


# Example 13
print("\nExample13 : normalize_defensive(list)")
visits = [15, 35, 80]
# 2016.06.10 change
#normalize_defensive(visits)  # No error
percentages = normalize_defensive(visits)  # No error
print(percentages)

print("\nExample 13 : normalize_defensive(specific-container)")    
visits = ReadVisits(path)
# 2016.06.10 change
#normalize_defensive(visits)  # No error
percentages = normalize_defensive(visits)  # No error
print(percentages)

# Example 14
print("\nExample 14 : normalize_defensive(iterator)")
try:
    it = iter(visits)
    normalize_defensive(it)
except:
    logging.exception('Expected')
else:
    assert False
