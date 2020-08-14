"""
LC797 - All paths from source to target

Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any
order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which
the edge (i, j) exists.

Example:
Input: [[1,2], [3], [3], []]
Output: [[0,1,3],[0,2,3]]
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
"""


class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        end_node = len(graph) - 1

        # so, we want to do this recursively:
        # all the ways to get to the end node from a node are all the ways to get to the end node from its children
        # with the node tacked onto the beginning

        # this gives us a list of all the paths, individually in reverse order
        ret = self.path_helper(graph, 0, end_node)
        return [r[::-1] for r in ret]

    def path_helper(self, graph, node, end_node):
        # this function should return a list of lists with paths to the end node from the current node, in
        # reverse order (i.e. last node first). This is so that we don't have to insert into position 0 each time
        # termination condition
        if node == end_node:
            return [[end_node]]
        else:
            r = []
            for child_node in graph[node]:
                paths = self.path_helper(graph, child_node, end_node)
                for path in paths:
                    r.append(path + [node])

            return r
