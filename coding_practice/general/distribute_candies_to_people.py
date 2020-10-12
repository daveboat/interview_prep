"""
LC1103 - Distribute candies to people

We distribute some number of candies, to a row of n = num_people people in the following way:

We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last
person.

Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person,
and so on until we give 2 * n candies to the last person.

This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the
end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more
than the previous gift).

Return an array (of length num_people and sum candies) that represents the final distribution of candies.

Example 1:

Input: candies = 7, num_people = 4
Output: [1,2,3,1]
Explanation:
On the first turn, ans[0] += 1, and the array is [1,0,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0,0].
On the third turn, ans[2] += 3, and the array is [1,2,3,0].
On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].

Example 2:

Input: candies = 10, num_people = 3
Output: [5,2,3]
Explanation:
On the first turn, ans[0] += 1, and the array is [1,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0].
On the third turn, ans[2] += 3, and the array is [1,2,3].
On the fourth turn, ans[0] += 4, and the final array is [5,2,3].

Constraints:

    1 <= candies <= 10^9
    1 <= num_people <= 1000
"""


from math import sqrt, ceil


class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        # first round distributes n(n+1)/2 candies to everyone. subsequent rounds add r*n^2 + n(n+1)/2
        # for each round. For R complete rounds, the ith person gets sum_r=0^R (rn+i) = (R+1)(nR/2 + i)
        # and the total candies distributed is sum_i=1^n (R+1)(nR/2 + i) = n^2R(R+1)/2 + n(n+1)(R+1)/2
        #
        # We can solve for R given the number of candies, i.e. n^2R(R+1)/2 + n(n+1)(R+1)/2 = C, which is
        # quadratic in R (a2R^2 + a1R + a0 = 0) with a2 = n^2/2, a1 = n^2 + n/2, a0 = (n^2 + n)/2 - C
        #
        # This quadratic has positive and negative real solutions as long as C > n(n+1)/2. We want
        # the positive root, or (sqrt(a1^2 - 4*a2*a0) - a1)/(2*a2), and we want to take the ceiling.
        #
        # Then, when adding full round candies, we use R-1 in place of R because, again, r is indexed
        # from 1 but there's an extra round in the beginning where r is 0. So if there's 1 full round
        # (R=1), then we only want to add the first round with n(n+1)/2 candies, and so forth.

        # This algorithm is O(N) in time and space. The O(N) in space is unavoidable for the return values.
        # The O(N) in time is also unavoidable, since you have to at least assign every element of the
        # return array.

        # step 1: solve for R, the number of full rounds we have
        n = num_people
        C = candies
        a2 = n ** 2 / 2
        a1 = n ** 2 + n / 2
        a0 = (n ** 2 + n) / 2 - C
        R = ceil((sqrt(a1 ** 2 - 4 * a2 * a0) - a1) / (2 * a2))

        # step 2: create an array with the full round candies (skip if R is 0)
        ans = [0] * n
        if R > 0:
            # subtract candies added from candy count
            C -= (R) * n * (n + 1) / 2 + n ** 2 * (R - 1) * R / 2
            for i in range(num_people):
                # remember that people are indexed starting from 1 but the array starts from 0, so we replace
                # i with i+1 in this formula
                c = (R) * (n * (R - 1) / 2 + i + 1)
                ans[i] = c

        # step 3: add remaining candies. the person at index i gets R*n + i + 1, or the remainder of the
        # candies, whichever is greater
        i = 0
        while C >= R * n + i + 1:
            ans[i] += R * n + i + 1
            C -= R * n + i + 1
            i += 1
        ans[i] += C  # add remainder

        return [int(i) for i in ans]

