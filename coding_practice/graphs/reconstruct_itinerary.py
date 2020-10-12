"""
LC332 - Reconstruct Itinerary

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the
itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
    If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when
    read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
    All airports are represented by three capital letters (IATA code).
    You may assume all tickets form at least one valid itinerary.
    One must use all the tickets once and only once.

Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""
import heapq


class Solution(object):
    def dfs(self, loc, adj, it):
        # visit each of the adjacent nodes for loc, popping them from the heap as we go
        if loc in adj:
            while adj[loc]:
                self.dfs(heapq.heappop(adj[loc]), adj, it)

        # when we return from dfs'ing, append the current node to our itinerary
        it.append(loc)

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        # i tried doing this with a dictionary and visiting nodes in order, but this doesn't work, because there can be
        # cases where nodes out of alphabetical order must be visited first in order to visit all the nodes, i.e. if a
        # node in alphabetical order is visited first, it can result in a dead end without all the other nodes being
        # visited
        #
        # a straightforward topological sort wont work either, because nodes need to be visited more than once
        #
        # my dictionary solution was basically a graph traversal where we choose to visit the next node in alphabetical
        # order
        #
        # The actual solution is to use a dictionary with a priority queue as our adjacency list, and depth first search
        # and pop adjacencies as we visit them. We add the nodes to our ordering once we return from them, in reverse
        # order. So the priority queue enforces that we visit in alphabetical order, and adding nodes to our itinerary
        # in reverse order when we recurse back from a node ensures we visit everything in the correct topological order
        #
        # So basically we do a post-order depth-first traversal, and then return in reverse traversal order
        #
        # The other option is a pre-order traversal. With a pre-order traversal, regardless of the order of the heap, we
        # would end up visiting nodes in the wrong order for some itineraries. An example of this is if there's a dead
        # end that we visit before the rest of the graph, then that dead end will appear before the rest of the graph in
        # our itinerary, which is in the wrong order

        # create our adjacency list with minheaps for ordering
        adj = dict()
        for fr, to in tickets:
            if fr not in adj:
                adj[fr] = [to]
            else:
                heapq.heappush(adj[fr], to)

        # create our itinerary list
        it = []

        # dfs, passing the adjacency dict and itinerary list
        self.dfs('JFK', adj, it)

        # return the itinerary list in reverse order
        return it[::-1]


if __name__ == '__main__':
    S = Solution()

    a = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    b = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
    c = [["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]

    print(S.findItinerary(b))