"""
LC1277 - Count square submatrices with all ones

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:

Input: matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation:
There are 6 squares of side 1.
There is 1 square of side 2.
Total number of squares = 6 + 1 = 7.

-----------------------------------------------------------------------------------------------------------------------

Given a mxn matrix with zeroes and ones, count the number of all possible square submatrices formed with ones. Single
ones count as square submatrices.
"""

import numpy as np


def generate_indices(row, col, k):
    """
    Generates indices for the inverse-L shaped region n blocks away. For example, for i, j = 1, 1 and k = 1, this should
    return [(1, 2), (2, 1), (2, 2)]. For the same i, j and k = 2, this should return [(1, 3), (2, 3), (3, 3), (3, 2), (3, 1)]

    This function doesn't take the size of the matrix into account, it just generates the raw indices as tuple of np arrays, for easy indexing
    """
    # row_out = []
    # col_out = []
    #
    # for i in range(0, k + 1):
    #     row_out.append(row + k)
    #     col_out.append(col + i)
    # for i in range(0, k):
    #     row_out.append(row + i)
    #     col_out.append(col + k)
    #
    # return (np.array(row_out), np.array(col_out))

    return [row+k] * (k+1) + [row + n for n in range(0, k)], [col + n for n in range(0, k + 1)] + [col + k] * k


class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        # # convert to np array for easier indexing
        # matrix = np.array(matrix)
        #
        # # get shape
        # m, n = matrix.shape
        #
        # # get size of maximum possible square
        # max_square_size = min(m, n)
        #
        # squares = 0
        #
        # # loop through the array
        # for row in range(m):
        #     for col in range(n):
        #         if matrix[row, col] == 1:
        #             squares += 1
        #             for k in range(1, min(m - row, n - col)):
        #                 if sum(matrix[generate_indices(row, col, k)]) == 2 * k + 1:
        #                     squares += 1
        #                 else:
        #                     break
        #
        # return squares

        # dynamic programming approach
        matrix = np.array(matrix)
        m, n = matrix.shape
        sum_matrix = np.zeros_like(matrix)

        for i in range(m):
            for j in range(n):
                if matrix[i, j] == 0:
                    sum_matrix[i, j] = 0
                else:
                    if i == 0 or j == 0:
                        sum_matrix[i, j] = 1
                    else:
                        sum_matrix[i, j] = 1 + min(sum_matrix[i-1, j], sum_matrix[i, j-1], sum_matrix[i-1, j-1])

        return np.sum(sum_matrix)


S = Solution()

matrix =[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

print(S.countSquares(matrix))