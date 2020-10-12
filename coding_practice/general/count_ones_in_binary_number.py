"""
LC338 - Counting Bits

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in
their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]

Example 2:

Input: 5
Output: [0,1,1,2,1,2]

Follow up:

    It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n)
    /possibly in a single pass?
    Space complexity should be O(n).
    Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other
    language.
"""


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        # the idea is that, after the first four counts ([0, 1, 1, 2]), the next eight are the first four, followed by
        # the first four plus 1, so [0, 1, 1, 2, 1, 2, 2, 3]. The next sixteen are the last eight, and then the last
        # eight plus 1, and so forth.

        base = [0, 1, 1, 2]
        add_counter = 2

        if len(base) > num + 1:
            return base[:num + 1]

        while len(base) < num + 1:
            base += base[-add_counter:]
            base += [x + 1 for x in base[-add_counter:]]

            add_counter *= 2

        return base[:num + 1]


if __name__ == '__main__':
    S = Solution()

    print(S.countBits(4))