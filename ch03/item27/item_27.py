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
print("Example 1-4 : public and private attribute")
class MyObject(object):
    def __init__(self):
        self.public_field = 5
        self.__private_field = 10

    def get_private_field(self):
        return self.__private_field


# Example 2
foo = MyObject()
assert foo.public_field == 5
print("foo.public_field:", foo.public_field)

# Example 3
assert foo.get_private_field() == 10
print("foo.get_private_field():", foo.get_private_field())

# Example 4
print("try to access foo.__private_field:")
try:
    foo.__private_field
except:
    logging.exception('Expected')
else:
    assert False


# Example 5
print("\nExample 5 : access private attribute from class-method")
class MyOtherObject(object):
    def __init__(self):
        self.__private_field = 71

    @classmethod
    def get_private_field_of_instance(cls, instance):
        return instance.__private_field

bar = MyOtherObject()
assert MyOtherObject.get_private_field_of_instance(bar) == 71
print("MyOtherObject.get_private_field_of_instance(bar):", MyOtherObject.get_private_field_of_instance(bar))


# Example 6
print("\nExample 6 : access private from sub-class")
try:
    class MyParentObject(object):
        def __init__(self):
            self.__private_field = 71
    
    class MyChildObject(MyParentObject):
        def get_private_field(self):
            return self.__private_field
    
    baz = MyChildObject()
    baz.get_private_field()
except:
    logging.exception('Expected')
else:
    assert False


# Example 7
print("\nExample 7-8 : direct access to private attribute")
assert baz._MyParentObject__private_field == 71
print("baz._MyParentObject__private_field:", baz._MyParentObject__private_field)

# Example 8
print(baz.__dict__)


# Example 9
print("\nExample 9-10 : patch problem by subclassing")
class MyClass(object):
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return str(self.__value)

foo = MyClass(5)
assert foo.get_value() == '5'


# Example 10
class MyIntegerSubclass(MyClass):
    def get_value(self):
        return int(self._MyClass__value)

foo = MyIntegerSubclass(5)
assert foo.get_value() == 5
print("foo.get_value():", foo.get_value())

# Example 11
print("\nExample 11-12 : base class was changed")
class MyBaseClass(object):
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

class MyClass(MyBaseClass):
    def get_value(self):
        return str(super().get_value())

class MyIntegerSubclass(MyClass):
    def get_value(self):
        return int(self._MyClass__value)


# Example 12
try:
    foo = MyIntegerSubclass(5)
    foo.get_value()
except:
    logging.exception('Expected')
else:
    assert False


# Example 13
print("\nExample 13 : use protected attribute")
class MyClass(object):
    def __init__(self, value):
        # This stores the user-supplied value for the object.
        # It should be coercible to a string. Once assigned for
        # the object it should be treated as immutable.
        self._value = value

    def get_value(self):
        return str(self._value)

class MyIntegerSubclass(MyClass):
    def get_value(self):
        return self._value

foo = MyIntegerSubclass(5)
assert foo.get_value() == 5
print("foo.get_value():", foo.get_value())

# Example 14
print("\nExample 14 : accidental batting of api's protected attribute")
class ApiClass(object):
    def __init__(self):
        self._value = 5

    def get(self):
        return self._value

class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello'  # Conflicts

a = Child()
print(a.get(), 'and', a._value, 'should be different')


# Example 15
print("\nExample 15 : use private attribute in api to avoid accident")
class ApiClass(object):
    def __init__(self):
        self.__value = 5

    def get(self):
        return self.__value

class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello'  # OK!

a = Child()
print(a.get(), 'and', a._value, 'are different')
