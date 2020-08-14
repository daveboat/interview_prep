"""
An alternative implementation of dijkstra's, where shortest path and parent calculations happen when we visit a node,
instead of when we push a node onto the heap
"""

import heapq


def dijkstras(graph_list, start):
    """
    For a graph as a list of adjacencies and weights List[[fr, to, w]], return a list of shortest paths to all nodes,
    and their shortest path values
    """
    # for returning
    shortest_dist = dict()
    shortest_parent = dict()

    # create an adjacency list from the graph definition, and a dict for keeping track of parents
    graph = {}  # our adjacency list dict
    parent = {}  # our parents dict

    for fr, to, w in graph_list:
        if fr not in graph:
            graph[fr] = [(to, w)]
        else:
            graph[fr].append((to, w))

        if fr not in parent:
            parent[fr] = None
        if to not in parent:
            parent[to] = None

    # in this implementation of dijkstras, we keep track of a list of visited nodes in order to use a heap as-is,
    # without having to modify the heap's weights
    visited = set()
    heap = [(0, start, None)]  # distance, node, parent

    while heap:
        curr_dist, node, par = heapq.heappop(heap)

        # only visit this node if it's not visited yet. The first time we visit a node, because of the heap, it's
        # guaranteed that it's the shortest path
        if node not in visited:
            # visit this node
            visited.add(node)

            # update shortest dict and parent dict
            shortest_dist[node] = curr_dist
            parent[node] = par

            # we won't visit this node again, so compute the parent list here
            curr_parent_list = []
            pnode = node
            # work out shortest parent
            while pnode:
                curr_parent_list.append(pnode)
                pnode = parent[pnode]
            shortest_parent[node] = curr_parent_list[::-1]

            # add adjacent nodes if they haven't been visited
            if node in graph:
                for to, w in graph[node]:
                    if to not in visited:
                        heapq.heappush(heap, (curr_dist + w, to, node))

    print(shortest_dist)
    print(shortest_parent)


if __name__ == '__main__':
    adj_list = [['A', 'B', 5], ['A', 'C', 1], ['C', 'D', 1], ['D', 'B', 1], ['B', 'E', 2]]

    dijkstras(adj_list, 'C')