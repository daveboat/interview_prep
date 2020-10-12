"""
LC96 - Unique binary search trees

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

------------------------------------------------------------------------------------------------------------------------

The answer to this question is the so-called Catalan sequence G(n). The combinatorial formula is
1/(n+1) * (2n choose n) = (2n)!/((n+1)!n!).

To see why, note that, for a particular tree with values up to i, we plant the values j = 1 to i at the root. For each
of these trees, the left subtree must contain the numbers from 1 to j-1, and the right subtree must contain the values
from j+1 to i. The right subtree is directly the previously computed solution for j-1, and the right subtree can be
considered the same as the previously computed solution for i-j, since it contains a contiguous sequence of i-j numbers.

So for each j, we accumulate G(j-1) * G(i-j), and we multiply here because we are counting the number of total
combinations with all possibilities in the left subtree with all possibilities in the right subtree.

For example, for i = 4, we have
     1                    2                3                4
    / \                  / \              / \              / \
  {}  {2, 3, 4}       {1}  {3, 4}    {1, 2}  {4}   {1, 2, 3}  {}

So the answer is G(0) * G(3) + G(1) * G(2) + G(2) * G(1) + G(3) * G(0) = 1 * 5 + 1 * 2 + 2 * 1 + 5 * 1 = 14
"""


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [1, 1, 2, 5]

        if n <= 3:
            return G[n]

        for i in range(4, n + 1):
            G.append(sum(G[j - 1] * G[i - j] for j in range(1, i+1)))

        return G[-1]


if __name__ == '__main__':
    S = Solution()

    S.numTrees(6)