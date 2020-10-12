"""
Leetcode 1029 - two city scheduling

There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and
the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation:
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

Note:

    1 <= costs.length <= 100
    It is guaranteed that costs.length is even.
    1 <= costs[i][0], costs[i][1] <= 1000

------------------------------------------------------------------------------------------------------------------------

The idea is to use two minheaps, one for people going to city A, one for people going to city B. For each [a, b] in
costs, if a < b, it's favorable for that person to go to city A, so we put him/her into heap A. Similarly, if b>a, it's
favorable for that person to go to city B, so we put him/her into heap B. However, when we insert into our heaps, we
insert based on the difference between a and b. If a==b, we insert into whichever heap has fewer people.

After the first pass of creating our heaps, we need to balance the heaps so that they contain equal numbers of people.
The key thing to remember is that, when we move a person from the larger heap to the smaller heap, we want to move the
one with the smallest absolute difference between a and b. In other words, we want to move a person who has the least
impact on the total cost -- in the limit, if a==b, we can move that person freely, because that move has no impact
whatsoever, so we start with moving people whose costs are very similar, and then go up from there.

The time complexity is O(NlogN), and the space complexity is O(N).
"""

import heapq


class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        heapA = []
        heapB = []

        # first pass, push onto heaps based on whether a<b or b>a, or a==b.
        # this is O(NlogN)
        for c in costs:
            a = c[0]
            b = c[1]

            # if a < b, push into heapA, but prioritized by b-a
            if a < b:
                heapq.heappush(heapA, (b - a, a, b))
            # if b < a, push into heapB, put prioritized by a-b
            elif a > b:
                heapq.heappush(heapB, (a - b, a, b))
            # if a == b, push onto whichever heap has fewer elements
            else:
                if len(heapA) <= len(heapB):
                    heapq.heappush(heapA, (0, a, b))
                else:
                    heapq.heappush(heapB, (0, a, b))

        # second pass, balance heaps. This is also O(NlogN)
        while len(heapA) != len(heapB):
            if len(heapA) < len(heapB):
                _, a, b = heapq.heappop(heapB)
                heapq.heappush(heapA, (b - a, a, b))
            else:
                _, a, b = heapq.heappop(heapA)
                heapq.heappush(heapB, (a - b, a, b))

        return sum([A[1] for A in heapA] + [B[2] for B in heapB])


if __name__ == '__main__':
    costs = [[518,518],[71,971],[121,862],[967,607],[138,754],[513,337],[499,873],[337,387],[647,917],[76,417]]

    S = Solution()

    print(S.twoCitySchedCost(costs))
