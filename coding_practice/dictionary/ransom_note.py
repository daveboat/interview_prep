"""
LC383 - Ransom note

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""


from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        if len(magazine) < len(ransomNote):
            return False

        r_count = Counter(ransomNote)
        m_count = Counter(magazine)

        for r_key in r_count.keys():
            if r_key not in m_count.keys() or m_count[r_key] < r_count[r_key]:
                return False

        return True