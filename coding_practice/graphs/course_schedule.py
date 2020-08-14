"""
LC207 - Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
"""


class Node:
    """
    The class definition for a graph node
    """

    def __init__(self, id):
        self.adjacent = set()  # a set (hashset) to store nodes which this node has an edge pointing to
        self.id = id  # this node's unique ID


class Graph:
    """
    The class object for a graph with directed or undirected edges
    """

    def __init__(self):
        self.node_dict = {}  # a dictionary of nodes keyed by their unique ID

    def __str__(self):
        return str(self.node_dict)

    def add_node(self, id):
        """
        Add a node to the graph
        """
        if id in self.node_dict:
            raise ValueError("Node with ID {} already exists".format(id))
        else:
            self.node_dict[id] = Node(id)

    def add_edge(self, source_id, dest_id, undirected=False):
        """
        Add an edge between source and dest nodes
        """
        self.get_node(source_id).adjacent.add(self.get_node(dest_id))
        if undirected:
            self.get_node(dest_id).adjacent.add(self.get_node(source_id))

    def get_node(self, id):
        """
        Return the Node object associated with an ID
        """
        return self.node_dict[id]


def detect_cycle(graph):
    """
    Returns True if a cycle exists in the graph. Uses the classic white/gray/black set depth first search algorithm

    Add all nodes to the white set. Start with any (iter(white).next()) node in the white set, and do our modified DFS
    on it. When we enter DFS, move the node from white set to gray set. For all adjacent nodes, if the node is in the
    black set, don't visit it. If it's in the gray set, then we've found a cycle. If it's in the white set, continue
    with DFS down that node. After returning from all children nodes (i.e. when returning from the recursive dfs
    function), move the node from the gray to the black set.
    """
    white = {node for node in graph.node_dict.values()}
    gray = set()
    black = set()

    while white:
        # grab a random node in the white set
        node = next(iter(white))
        # return true if the dfs search returns true, there was a cycle, otherwise keep going
        if _cycle_detection_dfs_helper(node, white, gray, black):
            return True

    # if we've gone through all the nodes, return false, no cycle
    return False


def _cycle_detection_dfs_helper(node, white, gray, black):
    # move node from white to gray
    white.remove(node)
    gray.add(node)

    # iterate through adjacent nodes
    for v in node.adjacent:
        # if v is in the black set, move on. We don't want to revisit nodes in the black set
        if v in black:
            continue

        # if v is in the gray set, return True now, since we've found a cycle
        if v in gray:
            return True

        # else (it must be in the white set), dfs with v, return True if the dfs returns True
        if _cycle_detection_dfs_helper(v, white, gray, black):
            return True

    # after finishing recursing, move this node from the gray set to the black set, and return False
    gray.remove(node)
    black.add(node)

    return False


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # initialize our graph object
        graph = Graph()

        # add nodes to the graph
        for i in range(numCourses):
            graph.add_node(i)

        # add edges to the graph
        for p in prerequisites:
            graph.add_edge(p[0], p[1])

        return not detect_cycle(graph)
