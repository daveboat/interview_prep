"""
LC835 - Image overlap

Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and
1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top
of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.

Notes:

    1 <= A.length = A[0].length = B.length = B[0].length <= 30
    0 <= A[i][j], B[i][j] <= 1
"""


class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        # (not my code, no time today). Idea is to:
        # 1. from the two arrays, get a list of all 1's in terms of rows and cols (O(N^2))
        # 2. from the lists, create a dictionary keyed by (x_B - x_A, y_B - y_A). Do a nested loop where
        # for each pair in the two lists, add 1 to each key. This keeps track of number of same pixels for every
        # translation.
        # 3. return the max value in the dictionary

        R = len(A)
        C = len(A[0])

        la = []
        lb = []

        v = collections.Counter()

        for r in range(R):
            for c in range(C):
                if A[r][c] == 1:
                    la.append((r, c))
                if B[r][c] == 1:
                    lb.append((r, c))

        for ax, ay in la:
            for bx, by in lb:
                k = (ax - bx, ay - by)
                v[k] += 1

        return max(v.values() or [0])
