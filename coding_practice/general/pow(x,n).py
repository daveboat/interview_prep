"""
LC50 - Pow(x,n)

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000

Example 2:

Input: 2.10000, 3
Output: 9.26100

Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Note:

    -100.0 < x < 100.0
    n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # so, we could just use the power operator, but that would be against the spirit of this example.
        # return x ** n

        # Instead, let's solve the following way:
        # Multiply the number by itself, to get x^2, then, multiply x^2 by itself to get x^4, and so on. Each time, we
        # subtract n by the current exponential (2, 4, etc). If n reaches 0, we return our number. If the remaining n
        # is smaller than or equal to the current exponent, then go down our recorded list of past values and multiply
        # by that, and so forth, until n reaches 0

        # we find the answer in O(logN) time and space complexity

        # trivial case
        if n == 0:
            return 1

        # transform for negative powers
        if n < 0:
            n *= -1
            x = 1 / x

        powers = [x]  # an array of powers, where each entry is x raised to 2^i
        i = 1  # index of the powers array that we're currently on, corresponding to x raised to 2 ^ i
        # the while loop
        power_counter = 2

        if n == 1:
            return x

        r = 1

        while n > 0:
            # if the remaining n is greater than or equal to power_counter, subtract n from the counter, multiply r
            # by powers[-1], and increment the power counter and index
            if n >= power_counter:
                powers.append(powers[-1] * powers[-1])
                n -= power_counter
                power_counter *= 2
                i += 1
                r *= powers[-1]
            # if n is less than the power counter, go in the opposite direction (divide power counter by 2, decrement
            # the index) until we find a power_counter that is larger than or equal to n. When we find that, multiply
            # r by powers[i], and subtract n by power_counter
            else:
                while n < power_counter:
                    power_counter //= 2
                    i -= 1
                n -= power_counter
                r *= powers[i]

        return r


if __name__ == '__main__':
    S = Solution()

    for i in range(-10, 10):
        print(S.myPow(2,i))