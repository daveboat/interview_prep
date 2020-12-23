"""
LC74 - Search in a 2D matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
Output: false

Example 3:

Input: matrix = [], target = 0
Output: false

Constraints:

    m == matrix.length
    n == matrix[i].length
    0 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104
"""

class Solution:
    def searchMatrix(self, matrix, target):
        # since the entire matrix is in order if we flatten the rows, this is just a straightforward binary search
        # of order log(rows*cols), except we need to address the matrix with [i // cols, i % cols]

        # trivial case
        if not matrix or not matrix[0]:
            return False

        cols = len(matrix[0])
        rows = len(matrix)

        left = 0
        right = rows * cols - 1

        while left < right:
            mid = (left + right) // 2

            if matrix[mid // cols][mid % cols] < target:
                left = mid + 1
            else:
                right = mid

        return matrix[left // cols][left % cols] == target
