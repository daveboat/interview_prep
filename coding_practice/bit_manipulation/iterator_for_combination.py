"""
LC1286 - Iterator for combination

Design an Iterator class, which has:

    A constructor that takes a string characters of sorted distinct lowercase English letters and a number
    combinationLength as arguments.
    A function next() that returns the next combination of length combinationLength in lexicographical order.
    A function hasNext() that returns True if and only if there exists a next combination.

Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false

Constraints:

    1 <= combinationLength <= characters.length <= 15
    There will be at most 10^4 function calls per test.
    It's guaranteed that all calls of the function next are valid.
"""


class CombinationIterator(object):
    def mask(self, string, bit_mask):
        # return the characters of the string where bit_mask is 1, assuming bit_mask doesn't have any 1's past the
        # length of the string
        ret = ''
        c = len(string) - 1

        while bit_mask:
            if bit_mask & 1:
                ret += string[c]
            bit_mask >>= 1
            c -= 1

        return ret[::-1]

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        # okay, let's try to use bit masking as the hint says, to generate our combinations
        self.comb = []
        N = len(characters)

        # I don't know of a way to generate all combinations of binary numbers with x ones, so let's just
        # loop through I guess. We loop from 2^N - 1 to 0 because that gives us the correct lexographical
        # order
        for i in range(2 ** N - 1, -1, -1):
            if bin(i).count('1') == combinationLength:
                print(bin(i))
                self.comb.append(self.mask(characters, i))

        # a counter for keeping track of where we are in our list
        self.counter = 0

    def next(self):
        """
        :rtype: str
        """
        ret = self.comb[self.counter]
        self.counter += 1
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.counter < len(self.comb)

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
