"""
Simple implementation of a directed acyclic graph in python, with depth-first and breadth-first path searches

TODO:

Undirected Graphs, adjacency matrices

https://pythonandr.com/2016/07/28/implementing-undirected-graphs-in-python/

Shortest path:

    Dijkstra's algorithm (weighted edges with non-negative edge weights)
    - https://www.youtube.com/watch?v=pSqmAO-m7Lk
    - https://www.youtube.com/watch?v=pVfj6mxhdMw

    Breadth-first search (unweighted edges)
    - https://medium.com/@yasufumy/algorithm-breadth-first-search-408297a075c9

    Bellman-Ford algorithm (weighted edges with positive and negative weights)
    - https://www.youtube.com/watch?v=lyw4FaxrwHg

Directed Acyclic Graphs:

    Topological sort - https://www.youtube.com/watch?v=eL-KzMXSXXI

Python library implementation of a graph

Undirected graphs and coloring
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
    The class object for a graph (DAG)
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

    def get_adjacency_matrix(self):
        """
        Returns the adjacency matrix as a List[List[int]]. Entries are in sorted() order by vertex ID
        """
        # get IDs in sorted order
        ids = sorted(self.node_dict)
        N = len(ids)

        # initialize adjacency matrix
        adj_matrix = [[0 for i in range(N)] for j in range(N)]

        # build adjacency matrix
        for id in ids:
            u = self.get_node(id)
            for v in u.adjacent:
                adj_matrix[ids.index(u.id)][ids.index(v.id)] = 1

        return adj_matrix

    def path_dfs(self, source_id, dest_id):
        """
        A DFS algorithm for whether the node with dest_id can be reached from the node with source_id
        """

        visited = set()  # create a set which contains nodes which have been visited
        source = self.get_node(source_id)
        dest = self.get_node(dest_id)
        return self._path_dfs_helper(source, dest, visited)

    def _path_dfs_helper(self, source, dest, visited):
        """
        This function uses actual nodes, not node ids
        """
        # if we've already visited this node, immediately return false
        if source in visited:
            return False
        # now, if we haven't visited this node, but the id is equal to the id we want, return True
        elif source == dest:
            return True
        # finally, if we haven't visited this node, add it to the set of visited nodes, and search its adjacent nodes
        else:
            visited.add(source)
            for node in source.adjacent:
                if self._path_dfs_helper(node, dest, visited):
                    return True
            return False

    def path_bfs(self, source_id, dest_id):
        """
        A BFS algorithm for whether or not there's a path from source to dest, using a queue
        """
        source = self.get_node(source_id)
        dest = self.get_node(dest_id)

        queue = [source]
        visited = {source}

        while queue:
            node = queue.pop(0)

            if node == dest:
                return True
            else:
                for adj_node in node.adjacent:
                    if adj_node not in visited:
                        queue.append(adj_node)

        return False


def detect_cycle(graph: Graph):
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


def _cycle_detection_dfs_helper(node: Node, white: set, gray: set, black: set):
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


def topsort(graph):
    """
    Find a topological ordering for a graph. Do this by selecting a node at random in the graph, and then doing a DFS,
    adding the node to the topological ordering in reverse order when the DFS recursive function returns from that node
    """
    unvisited = set(graph.node_dict.values())
    top_ordering = []

    while unvisited:
        start_node = next(iter(unvisited))
        _topsort_dfs_helper(start_node, unvisited, top_ordering)

    return top_ordering[::-1]


def _topsort_dfs_helper(node, unvisited, top_ordering):
    # if we've already visited this node, return immediately
    if node not in unvisited:
        return
    else:
        # set this node as visited
        unvisited.remove(node)

        # recurse into adjacent nodes
        for adj_node in node.adjacent:
            _topsort_dfs_helper(adj_node, unvisited, top_ordering)

        # when we return from this node, add its id to the topological ordering
        top_ordering.append(node.id)


if __name__ == '__main__':
    g = Graph()

    g.add_node('A')
    g.add_node('B')
    g.add_node('C')
    g.add_node('D')
    g.add_node('E')
    g.add_node('F')
    g.add_node('G')
    g.add_node('H')

    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'H')
    g.add_edge('C', 'F')
    g.add_edge('C', 'G')
    g.add_edge('C', 'D')
    g.add_edge('D', 'H')
    g.add_edge('D', 'E')

    # print(g.path_dfs('G', 'H'))
    # print(g.path_bfs('A', 'H'))
    #
    # print(g.get_adjacency_matrix())

    print(topsort(g))

    print(detect_cycle(g))
