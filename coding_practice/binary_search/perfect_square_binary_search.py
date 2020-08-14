"""
LC367 - Valid perfect square

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

Example 1:

Input: num = 16
Output: true

Example 2:

Input: num = 14
Output: false
"""


def isPerfectSquare(num):
    """
    :type num: int
    :rtype: bool
    """
    # brute force
    # for i in range(num + 1):
    #     i_squared = i * i
    #     if i_squared > num:
    #         return False
    #     elif i_squared == num:
    #         return True

    # binary search
    if num < 2:
        return True
    start = 1
    end = num // 2 + 1 if num < 5 else num // 2

    while start < end - 1:
        mid = (start + end) // 2
        mid_squared = mid * mid
        if mid_squared == num:
            return True
        elif mid_squared > num:
            end = mid
        else:
            start = mid

    return False


def ips(n):
    if n < 2:
        return True

    left = 1
    right = n // 2

    while left <= right:
        mid = (left + right) // 2
        mid_sq = mid * mid

        if mid_sq == n:
            return True
        elif mid_sq < n:
            left = mid + 1
        else:
            right = mid - 1

    return False


# print(isPerfectSquare(4))

for i in range(100):
    print(i, ips(i))