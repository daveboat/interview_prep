"""
LC278 - First bad version

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of
your product fails the quality check. Since each version is developed based on the previous version, all the versions
after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following
ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find
the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n

        if isBadVersion(1):
            return 1

        # binary search
        while start <= end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                end = mid - 1
            else:
                if isBadVersion(mid + 1):
                    return mid + 1
                start = mid + 1

        return end


# another version, doing exactly log(N) calls, without the extra initial and extra checking calls

class Solution1(object):
    def firstBadVersion(self, n):

        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1

        return right + 1