"""
LC859 - Buddy strings

Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result is equal to
B, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at
A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

Example 1:

Input: A = "ab", B = "ba"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.

Example 2:

Input: A = "ab", B = "ab"
Output: false
Explanation: The only letters you can swap are A[0] = 'a' and A[1] = 'b', which results in "ba" != B.

Example 3:

Input: A = "aa", B = "aa"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'a' to get "aa", which is equal to B.

Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true

Example 5:

Input: A = "", B = "aa"
Output: false

Constraints:

    0 <= A.length <= 20000
    0 <= B.length <= 20000
    A and B consist of lowercase letters.
"""



import string


class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        # trivial case
        if len(A) != len(B):
            return False

        # so if we are to return true, then A and B must have differences at exactly two indices and the letters
        # at those indices must be transposes of each other, or no differences and A must have at least one repeat
        # character. We can check for both in O(N) time and O(1) space

        d = {c: 0 for c in string.ascii_lowercase}  # to count letters

        num_differences = 0  # to count differences
        difference_indices = []
        repeat_character = False

        for i in range(len(A)):  # len(A) == len(B)
            d[A[i]] += 1
            if d[A[i]] > 1:
                repeat_character = True
            if A[i] != B[i]:
                num_differences += 1
                difference_indices.append(i)

            if num_differences > 2:
                return False

        if (num_differences == 2 and A[difference_indices[0]] == B[difference_indices[1]] and A[
            difference_indices[1]] == B[difference_indices[0]]) or (num_differences == 0 and repeat_character == True):
            return True
        else:
            return False
