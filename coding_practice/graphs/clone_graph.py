"""
LC133 - Clone Graph

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:

For simplicity sake, each node's value is the same as the node's index (1-indexed). For example, the first node with
val = 1, the second node with val = 2, and so on. The graph is represented in the test case using an adjacency list.

Adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of
neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to
the cloned graph.

Example 1:

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:

Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does
not have any neighbors.

Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.

Example 4:

Input: adjList = [[2],[1]]
Output: [[2],[1]]

Constraints:

    1 <= Node.val <= 100
    Node.val is unique for each node.
    Number of Nodes will not exceed 100.
    There is no repeated edges and no self-loops in the graph.
    The Graph is connected and all nodes can be visited starting from the given node.
"""


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # trivial case
        if not node:
            return None

        # so let's do a bfs through the original graph, making a new graph along the way. We do this by
        # keeping track of newly created copy nodes, keyed by their value, in a dictionary. Each time
        # we visit a new node in the original graph, we add its value, keyed to a newly copied node, into
        # the dictionary.
        # when a newly created node has a previously visited node in its neighbors, we only add that
        # node to its neighbors, instead of adding it to the queue and making a new copy node.
        # we can keep track of which copy nodes we've created by looking at the values in the dictionary.

        # make the dict and queue
        copy_node_dict = dict()
        queue = [node]

        # make the root node in the copy graph
        copy_root = Node(node.val)
        copy_node = copy_root
        copy_node_dict[node.val] = copy_node

        while queue:
            # get the node in the original graph that we are visiting
            original_node = queue.pop(0)

            # iterate through the neighbors of the original node
            for neighbor_node in original_node.neighbors:
                # if we haven't created a copy of a neighbour yet, we need to add it to the queue to visit it,
                # and make a copy node for it.
                if neighbor_node.val not in copy_node_dict:
                    queue.append(neighbor_node)
                    # make the new copy node
                    copy_node_dict[neighbor_node.val] = Node(neighbor_node.val)

                # make sure this copy node has every neighbor that the original node had. We don't need
                # to do anything special here except exhaustively add neighbor nodes, since the graph
                # is undirected
                copy_node_dict[original_node.val].neighbors.append(copy_node_dict[neighbor_node.val])

        return copy_node_dict[1]