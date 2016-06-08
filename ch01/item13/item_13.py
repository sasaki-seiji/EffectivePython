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
print("Example 1(try/finally)")
handle = open('random_data.txt', 'w', encoding='utf-8')
handle.write('success\nand\nnew\nlines')
handle.close()
handle = open('random_data.txt')  # May raise IOError
try:
    data = handle.read()  # May raise UnicodeDecodeError
finally:
    handle.close()        # Always runs after try:

print(data)

# Example 2
import json

def load_json_key(data, key):
    try:
        result_dict = json.loads(data)  # May raise ValueError
    except ValueError as e:
        raise KeyError from e
    else:
        return result_dict[key]         # May raise KeyError

# JSON decode successful
print("\nExample 2(JSON decode and key access successful)")
assert load_json_key('{"foo": "bar"}', 'foo') == 'bar'
print(load_json_key('{"foo": "bar"}', 'foo'))

print("\nExample 2(JSON decode sccessful but key access fails)")
try:
    load_json_key('{"foo": "bar"}', 'does not exist')
    assert False
except KeyError:
    pass  # Expected
    print("KeyError")

# JSON decode fails
print("\nExample 2(JSON decode fails)")
try:
    load_json_key('{"foo": bad payload', 'foo')
    assert False
except KeyError:
    pass  # Expected
    print("KeyError")


# Example 3
import json
UNDEFINED = object()

def divide_json(path):
    handle = open(path, 'r+')   # May raise IOError
    try:
        data = handle.read()    # May raise UnicodeDecodeError
        op = json.loads(data)   # May raise ValueError
        value = (
            op['numerator'] /
            op['denominator'])  # May raise ZeroDivisionError
    except ZeroDivisionError as e:
        return UNDEFINED
    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)    # May raise IOError
        return value
    finally:
        handle.close()          # Always runs

# Everything works
print("\nExample 3(everything works)")
temp_path = 'random_data.json'
handle = open(temp_path, 'w')
handle.write('{"numerator": 1, "denominator": 10}')
handle.close()
assert divide_json(temp_path) == 0.1
print(divide_json(temp_path))

# Divide by Zero error
print("\nExample 3(Divide by Zero error)")
handle = open(temp_path, 'w')
handle.write('{"numerator": 1, "denominator": 0}')
handle.close()
assert divide_json(temp_path) is UNDEFINED
print(divide_json(temp_path))

# JSON decode error
print("\nExample 3(JSON decode error)")
handle = open(temp_path, 'w')
handle.write('{"numerator": 1 bad data')
handle.close()
try:
    divide_json(temp_path)
    assert False
except ValueError:
    pass  # Expected
    print("ValueError")