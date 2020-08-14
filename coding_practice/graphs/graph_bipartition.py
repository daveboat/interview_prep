"""
Seeing if a graph defined as a series of edges is bipartite, using a graph coloring algorithm
"""


class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """

        # Create an undirected graph, check if the graph is bipartite with a coloring algorithm.
        # The problem is when there are more than one graph sections which are disconnected. Therefore, we have to
        # keep track of which nodes have been visited, and run the coloring algorithm until all of the nodes have
        # been visited

        # create adjacency matrix. Note that the adjacency matrix is indexed starting from 0 but the edges (dislikes)
        # are indexed from 1. After this, we'll switch to indexing from 0 to N-1 instead of 1 to N
        adjacency = [[0 for i in range(N)] for j in range(N)]
        for dislike in dislikes:
            adjacency[dislike[0] - 1][dislike[1] - 1] = 1
            adjacency[dislike[1] - 1][dislike[0] - 1] = 1

        # create visited set, for keeping track of which nodes we've visited
        unvisited = {i for i in range(N)}

        # create a color array, for keeping track of colors
        colors = [-1] * N

        # outer loop to make sure we visit every node
        while unvisited:
            # choose a vertex from the unvisited set and add it as the first element of our breadth first search queue
            u = unvisited.pop()
            queue = [u]

            # assign the initial vertex a color
            colors[u] = 1

            # inner loop for BFS
            while queue:
                u = queue.pop(0)

                # for each neighbour of u, if it already has the same color as u, return False. else, assign it the
                # opposite color as u
                for v in range(N):
                    if adjacency[u][v] == 1:
                        # v has been visited
                        if v in unvisited:
                            unvisited.remove(v)

                        # if v hasn't been assigned a color, assign it the opposite of colors[u], and add it to the
                        # queue
                        if colors[v] == -1:
                            colors[v] = 1 - colors[u]
                            queue.append(v)
                        # if colors[v] has been assigned and it's the same as colors[u], then return false immediately
                        else:
                            if colors[v] == colors[u]:
                                return False

        # here, we're sure that we've visited every node and assigned colors to every node without a collision, so we
        # return True
        return True


if __name__ == '__main__':
    S = Solution()

    N = 3
    dislikes = [[1,2],[1,3],[2,3]]
    print(S.possibleBipartition(N, dislikes))

    N = 10
    dislikes = [[4,7],[4,8],[2,8],[8,9],[1,6],[5,8],[1,2],[6,7],[3,10],[8,10],[1,5],[7,10],[1,10],[3,5],[3,6],[1,4],[3,9],[2,3],[1,9],[7,9],[2,7],[6,8],[5,7],[3,4]]

    print(S.possibleBipartition(N, dislikes))
