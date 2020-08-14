"""
Build an array from subsequences, i.e. given
[[1, 3, 5], [2, 4, 6], [3, 4, 5]]

[1, 2, 3, 4, 5, 6] is a valid array, so is [1, 3, 2, 4, 5, 6]
"""

from graphs.graph_impl import Graph, topsort


def array_from_subsequences(subsequences):
    """
    subsequences: List[List[int]]
    """

    # create graph
    graph = Graph()

    # build directed graph from subsequences
    for subsequence in subsequences:
        if subsequence[0] not in graph.node_dict:
            graph.add_node(subsequence[0])
        for i in range(len(subsequence) - 1):
            if subsequence[i+1] not in graph.node_dict:
                graph.add_node(subsequence[i+1])
            graph.add_edge(subsequence[i], subsequence[i+1])

    return topsort(graph)


if __name__ == '__main__':
    subsequences = [[1, 2, 3], [1, 3, 5], [2, 4, 6], [3, 4, 5]]

    print(array_from_subsequences(subsequences))