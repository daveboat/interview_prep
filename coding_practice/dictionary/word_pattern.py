"""
LC290 - Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a
single space.
"""


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # easy, using a dictionary, eh?

        # step 1: split str into a list
        str = str.split()

        if len(pattern) != len(str):
            return False

        d = dict()

        for letter, word in zip(pattern, str):
            if word not in d.values():
                if letter not in d:
                    d[letter] = word
                else:
                    return False
            else:
                if letter not in d or d[letter] != word:
                    return False

        return True
