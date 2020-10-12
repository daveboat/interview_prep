"""
An implementation of Djikstra's algorithm, from scratch (no graph class or anything)

Based on this code:
https://leetcode.com/problems/network-delay-time/discuss/329376/efficient-oe-log-v-python-dijkstra-min-heap-with-explanation
"""

import collections
import heapq


def djikstras(n, edge_weights, src):
    """
    Djikstra's algorithm for a directed graph, returning a list of the shortest paths to each vertex. We assume the
    vertices have ids in [0, n-1]

    n: number of vertices in the graph
    edge_weights: a list of lists or tuples (source_vertex, dest_vertex, weight)
    src: source vertex id
    """

    # first, use a defaultdict to create our adjacency list. Could also make an adjacency matrix
    graph = collections.defaultdict(dict)

    for s, d, w in edge_weights:
        graph[s][d] = w

    # next, we need to keep track of: our distances, our visited vertices, and we need a minheap for keeping track of
    # greedy djikstra's. If we want to keep track of order, then we should create a parent dict also
    distances = {i: float("inf") for i in range(n)}
    distances[src] = 0
    heap = [(0, src)]
    visited = set()
    parents = {i: None for i in range(n)}

    # the algorithm works as follows:
    # - we start with the source vertex in our heap, with distance 0.
    # - We heappop a vertex from our heap, and add it to our visited set.
    # - For neighbours of our current vertex, if they are in our visited set, do nothing
    # - For neighbours of our current vertex not in the visited set, if the distance (distance of current vertex plus
    # the distance between the current vertex and the neighbour vertex) is less than the value in the distance dict,
    # push it into the heap with that distance and update the distance dict
    #
    # Note that this last step is a modification to the classic algorithm -- in the classic case, we would go into the
    # heap and modify neighbours' distances so that they have the lesser of their current distance and the new distance.
    # Here, bypass that by allowing ourselves to have duplicates in the heap, and rely on the fact that the copy with
    # the smallest distance will be popped first, and then use the visited set to make sure we don't do anything if we
    # see that vertex again.
    while heap:
        dist, vertex = heapq.heappop(heap)  # pop the smallest distance vertex from our heap
        visited.add(vertex)  # add this vertex to our visited pile

        # for each neighbour, push onto our heap with the correct distance if we haven't visited it yet, and if the
        # cumulative distance is less than what's currently recorded in the distance dict
        for neighbour in graph[vertex]:
            if neighbour in visited: continue

            neighbour_dist = dist + graph[vertex][neighbour]  # calculate current dist to the neighbour
            if neighbour_dist < distances[neighbour]:  # if the current dist is better than the recorded dist
                distances[neighbour] = neighbour_dist  # update the distance dict for this neighbour vertex
                parents[neighbour] = vertex  # update the parent for this neighbour vertex
                heapq.heappush(heap, (neighbour_dist, neighbour))  # push the neighbour with the calculated dist onto the heap

    return distances, parents


if __name__ == '__main__':
    e = [(0, 1, 100), (0, 2, 300), (1, 2, 100)]

    print(djikstras(3, e, 0))
