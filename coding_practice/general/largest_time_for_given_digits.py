"""
LC949 - Largest time for given digits
Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has
elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

Example 1:

Input: [1,2,3,4]
Output: "23:41"

Example 2:

Input: [5,5,5,5]
Output: ""

Note:

    A.length == 4
    0 <= A[i] <= 9
"""

class Solution(object):
    def is_valid(self, time):
        # luckily, python lets us compare strings like integers. This is okay because time must be in the format
        # 'hh:mm'
        return time[:2] < '24' and time[3:] < '60'

    def greater_than(self, time1, time2):
        # always return true if the time compared against is empty
        if len(time2) < 5:
            return True

        # returns true if time1 > time2. Again, we take advantage of the fact that python lets us compare strings
        # like this
        if time1[:2] > time2[:2]:
            return True
        elif time1[:2] == time2[:2]:
            return time1[3:] > time2[3:]
        else:
            return False

    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        # This is trickier than one might first think.
        # for example, with the numbers [1, 7, 2, 9], if we put 2 in the first position, then 1 must go into the second
        # and the rest can't fit. So we have to put 1 in the first position, followed by 9, then 2, then 7. In general
        # the trick is to design an algorithm that can detect when to do the greedy thing and put the largest value
        # in the most significant remaining place, and when another number needs to go in to satisfy the validity
        # requirement. I can't think of anything to do this except to do brute force... but we only have 4 digits,
        # so everything is automatically O(1). We can be clever though, and reduce the problem from four nested loops
        # to three nested loops by using the fact that no two indices can be the same, so the fourth index is known
        # if the other three are set

        # so we just check everything
        result = ''
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    if i == j or j == k or k == i:
                        continue
                    # since no two indices can be the same (we can't use a value twice), the fourth index must be
                    # (1+2+3 - i - j - k). So we can make the algorithm only have 3 nested loops instead of four
                    l = 6 - i - j - k
                    time = str(A[i]) + str(A[j]) + ':' + str(A[k]) + str(A[l])
                    if self.is_valid(time) and self.greater_than(time, result):
                        result = time
        return result
