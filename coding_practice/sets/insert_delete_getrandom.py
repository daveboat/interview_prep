"""
LC380 - Insert Delete Getrandom O(1)

Design a data structure that supports all following operations in average O(1) time.

    insert(val): Inserts an item val to the set if not already present.
    remove(val): Removes an item val from the set if present.
    getRandom: Returns a random element from current set of elements. Each element must have the same probability of
    being returned.

Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
"""

import random


class RandomizedSet(object):
    # we use a set data type directly for this. could also use a dict
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = set()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.s:
            return False
        else:
            self.s.add(val)
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.s:
            self.s.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(tuple(self.s))


class RandomizedSet2:
    """
    Another try without using sets, which is sort of cheating.

    We keep added elements in a list, and we track the index of those elements in the list with a dictionary. When an
    element is added, we update the dictionary and list appropriately. When an element is removed, we swap it with the
    last element, updating as appropriate, and then pop the last element and corresponding index entry
    """
    def __init__(self):
        self.idx = dict()
        self.vals = []

    def insert(self, val):
        if val not in self.idx:
            self.idx[val] = len(self.vals)
            self.vals.append(val)
            return True
        else:
            return False

    def remove(self, val):
        if val in self.idx:
            self.__swap(self.idx[val], len(self.vals) - 1)
            self.idx.pop(self.vals.pop())
            return True
        else:
            return False

    def getRandom(self):
        return random.choice(self.vals)

    def __swap(self, i, j):
        # swap the values in the list, and also the stored index
        self.vals[i], self.vals[j] = self.vals[j], self.vals[i]
        self.idx[self.vals[i]], self.idx[self.vals[j]] = self.idx[self.vals[j]], self.idx[self.vals[i]]