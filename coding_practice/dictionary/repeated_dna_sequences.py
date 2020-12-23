"""
LC187 - Repeated DNA sequences

All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". When
studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]

Constraints:

    0 <= s.length <= 105
    s[i] is 'A', 'C', 'G', or 'T'.
"""


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # strings are hashable, so we can hash all length 10 strings into a dictionary
        d = dict()
        for i in range(10, len(s) + 1):
            seq = s[i - 10:i]
            if seq not in d:
                d[seq] = 1
            else:
                d[seq] += 1

        return [key for key in d if d[key] > 1]
