gma"""
LC470 - Implement rand10() using rand7()

Given the API rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which
generates a uniform random integer in the range 1 to 10. You can only call the API rand7 and you shouldn't call any
other API. Please don't use the system's Math.random().

Notice that Each test case has one argument n, the number of times that your implemented function rand10 will be called
while testing.

Follow up:

    What is the expected value for the number of calls to rand7() function?
    Could you minimize the number of calls to rand7()?

Example 1:

Input: n = 1
Output: [2]

Example 2:

Input: n = 2
Output: [2,8]

Example 3:

Input: n = 3
Output: [3,8,10]

Constraints:

    1 <= n <= 105
"""


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        # we want to think of this in the following way:
        # we treat rolling a 7 as choosing digits in a base-7 number. So rolling the first number is
        # the least significant digit, 0 to 6. The second number is the next digit, 0 to 6 times 7 (10 in base 7), and
        # so forth. we keep going until we reach a number larger than the number we need, which is 10 in base 10.
        # rolling 2 7's gives us numbers from 0 to 48 in this way, represented as (rand7()-1) + (rand7()-1)*7
        #
        # this ensures that all numbers from 0 to 48 are uniformly distributed. Note that rolling twice and adding
        # the results, then rerolling if the result is over 9 does not result in a uniform distribution, since numbers
        # in the middle of the range are more likely to appear as a sum than numbers at the edges of the range.
        #
        # to get a random number from 0 to 9 (we just need to add 1 to get 10) from a random number from 0 to 48,
        # we sample with replacement, so if we get a number from 0 to 39, we take the number mod 10. if we get a
        # a number from 40 to 48, we reroll.

        r = (rand7() - 1) + (rand7() - 1) * 7
        while r > 39:
            r = (rand7() - 1) + (rand7() - 1) * 7

        return r % 10 + 1
