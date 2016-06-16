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
print("Example 1-2 : subclass of list")
class FrequencyList(list):
    def __init__(self, members):
        super().__init__(members)

    def frequency(self):
        counts = {}
        for item in self:
            counts.setdefault(item, 0)
            counts[item] += 1
        return counts


# Example 2
foo = FrequencyList(['a', 'b', 'a', 'c', 'b', 'a', 'd'])
print('Length is', len(foo))
foo.pop()
print('After pop:', repr(foo))
print('Frequency:', foo.frequency())


# Example 3
class BinaryNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Example 4
print("\nExample 4-5 : __getitem__()")
bar = [1, 2, 3]
print("bar:", bar)
bar[0]
print("bar[0]:", bar[0])

# Example 5
bar.__getitem__(0)
print("bar.__getitem__(0):", bar.__getitem__(0))


# Example 6
print("\nExample 3,6-8 : IndexableNode")
class IndexableNode(BinaryNode):
    def _search(self, count, index):
        found = None
        if self.left:
            found, count = self.left._search(count, index)
        if not found and count == index:
            found = self
        else:
            count += 1
        if not found and self.right:
            found, count = self.right._search(count, index)
        return found, count
        # Returns (found, count)

    def __getitem__(self, index):
        found, _ = self._search(0, index)
        if not found:
            raise IndexError('Index out of range')
        return found.value


# Example 7
tree = IndexableNode(
    10,
    left=IndexableNode(
        5,
        left=IndexableNode(2),
        right=IndexableNode(
            6, right=IndexableNode(7))),
    right=IndexableNode(
        15, left=IndexableNode(11)))


# Example 8
print('LRR =', tree.left.right.right.value)
print('Index 0 =', tree[0])
print('Index 1 =', tree[1])
print('11 in the tree?', 11 in tree)
print('17 in the tree?', 17 in tree)
print('Tree is', list(tree))


# Example 9
print("\nExample 9 : IndexableNode has no len() method")
try:
    len(tree)
except:
    logging.exception('Expected')
else:
    assert False


# Example 10
print("\nExample 10-11 : SequenceNode having __len__() derives IndexableNode")
class SequenceNode(IndexableNode):
    def __len__(self):
        _, count = self._search(0, None)
        return count


# Example 11
tree = SequenceNode(
    10,
    left=SequenceNode(
        5,
        left=SequenceNode(2),
        right=SequenceNode(
            6, right=SequenceNode(7))),
    right=SequenceNode(
        15, left=SequenceNode(11))
)

print('Tree has %d nodes' % len(tree))


# Example 12
print("\nExample 12 : BadType deriving Sequence is still abstract")
try:
    from collections.abc import Sequence
    
    class BadType(Sequence):
        pass
    
    foo = BadType()
except:
    logging.exception('Expected')
else:
    assert False


# Example 13
print("\nExample 13 : inherit SequenceNode(having __getitem__, __len__) and Sequence(having index, count)")
class BetterNode(SequenceNode, Sequence):
    pass

tree = BetterNode(
    10,
    left=BetterNode(
        5,
        left=BetterNode(2),
        right=BetterNode(
            6, right=BetterNode(7))),
    right=BetterNode(
        15, left=BetterNode(11))
)

print('Index of 7 is', tree.index(7))
print('Count of 10 is', tree.count(10))
