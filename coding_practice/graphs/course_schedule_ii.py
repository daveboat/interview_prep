"""
LC210 - Course schedule II

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as
a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to
finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses,
return an empty array.

Example 1:

Input: 2, [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
             course 0. So the correct course order is [0,1] .

Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

------------------------------------------------------------------------------------------------------------------------

So, for this question we need to return a topological sorting of the graph if a topological sorting is possible, or an
empty array if a topological sorting is impossible. To do this, we use the same cycle detection algorithm as in course
schedule I, but update it to also add the topological ordering of the nodes to a list. Very simple.

This works because the cycle detection traversal order is the same as for topsort, so we just do both at the same time.
"""


def detect_cycle(adj_list, n, top_order):
    # detect whether there's a cycle or not in a graph with nodes labeled by 0 through n-1, with the adjacency list
    # given as a dict of {node: [adj nodes]}

    white = set(i for i in range(n))
    gray = set()
    black = set()

    while white:
        node = next(iter(white))

        if detect_cycle_dfs_helper(adj_list, node, white, gray, black, top_order):
            return True

    return False


def detect_cycle_dfs_helper(adj_list, node, white, gray, black, top_order):
    white.remove(node)
    gray.add(node)

    for adj_node in adj_list[node]:
        if adj_node in black:
            continue
        if adj_node in gray:
            return True
        if detect_cycle_dfs_helper(adj_list, adj_node, white, gray, black, top_order):
            return True

    gray.remove(node)
    black.add(node)
    top_order.append(node)

    return False


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # so, this is a graph topological sorting question. We need to detect if there's a cycle, which we can do
        # with the three set algorithm. Then, we can use a topological sort to create the correct ordering.
        # we can actually do both in a single pass: do the white/gray/black set algorithm, which returns whether the
        # graph has a cycle in it or not, and add the node to the topological ordering at the same time

        # first, let's create the adjacency list!
        adj_list = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)

        top_order = []

        # next, we do our cycle detection and topsort at the same time
        if not detect_cycle(adj_list, numCourses, top_order):
            return top_order[::-1]
        else:
            return []
