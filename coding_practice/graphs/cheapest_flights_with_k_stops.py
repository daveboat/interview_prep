"""
LC787 - Cheapest flights with k stops

There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the
cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph looks like this:

The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

Example 2:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph looks like this:

The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
"""

from collections import defaultdict
import heapq


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """

        # we use a modified djikstra's algorithm, where we keep track of the number of stops, and we add every vertex
        # onto the heap as long as we are within our stop limit. Then, the heap pop order will give us the shortest
        # distance within our stop allowance

        # make our graph adjacency list
        graph = defaultdict(dict)
        for s, d, weight in flights:
            graph[s][d] = weight

        # We need a heap. This heap will be (current_cost, vertex_id, number_of_stops)
        heap = [(0, src, 0)]

        # begin our loop
        while heap:
            curr_cost, curr_vertex, curr_stops = heapq.heappop(heap)

            # check for dst. Since we're pushing onto our heap with priprity equal to the lowest distance from src,
            # by the time we visit dst, it is guaranteed to have the lowest possible cost
            if curr_vertex == dst:
                return curr_cost

            # neigobour loop. here's where djikstra's is modified. We want to push every vertex onto the heap that has
            # a number of stops less than the allowed stops. All neighbours of this node has the same number of
            # stops for this path
            neighbour_stops = curr_stops + 1
            if neighbour_stops <= K + 1:  # the <= K+1 here is because a single flight counts as 0 stops
                for neighbour in graph[curr_vertex]:
                    # compute distance along this particular path
                    neighbour_cost = curr_cost + graph[curr_vertex][neighbour]

                    # push neighbour onto heap
                    heapq.heappush(heap, (neighbour_cost, neighbour, neighbour_stops))

        # if we've left our loop, it means we couldn't add dst to the heap due to it exceeding the number of stops, so
        # return -1
        return -1


if __name__ == '__main__':
    S = Solution()

    """
    5
    [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
    0
    2
    2
    """
    n = 5
    edges = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]

    src = 0
    dst = 2
    K = 2

    print(S.findCheapestPrice(n, edges, src, dst, K))