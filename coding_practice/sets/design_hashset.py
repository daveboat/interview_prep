"""
LC705 - Design Hashset

Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

    add(value): Insert a value into the HashSet.
    contains(value) : Return whether the value exists in the HashSet or not.
    remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);
hashSet.add(2);
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);
hashSet.contains(2);    // returns true
hashSet.remove(2);
hashSet.contains(2);    // returns false (already removed)

Note:

    All values will be in the range of [0, 1000000].
    The number of operations will be in the range of [1, 10000].
    Please do not use the built-in HashSet library.
"""


class MyHashSet(object):
    # We implement this set by keeping a list of buckets (ie a list of lists), and using a hash function to
    # pick which bucket to append a value to. We use a simple hash function, hash = key % self.buckets
    # This hash function chooses which bucket to put each key into. The hash function is not unique for each number from
    # 0 to 1000000, so there's a tradeoff between the time each operation takes (having to potentially search through
    # multiple values in a bucket due to hash collision) and space complexity (having a larger number of buckets)
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 997
        self.set = [[] for _ in range(self.buckets)]

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        h = self._hash(key)
        if key not in self.set[h]:
            self.set[h].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        h = self._hash(key)
        if key in self.set[h]:
            self.set[h].remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        h = self._hash(key)
        return key in self.set[h]

    def _hash(self, key):
        return key % self.buckets

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)