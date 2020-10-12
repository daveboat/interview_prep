"""
LC459 - Repeated Substring Pattern

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the
substring together. You may assume the given string consists of lowercase English letters only and its length will not
exceed 10000.

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:

Input: "aba"
Output: False

Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # so, the longest possible repeating substring is len(s)//2
        # also, s[0:...] must be the start of all valid repeating substrings, and s[...:-1] must be the end of
        # all valid repeating substrings
        # Can we do this in O(N)?
        # we need to be careful of cases like 'abcabcabcxabcabcabcx'
        # so if we iterate up to len(s)//2 with loop index i, then we can keep track of the longest nonrepeating
        # substring.
        #
        # - initialize the repeating substring with s[0], and substring index r = 0
        # - loop through s from 1 to len(s) // 2 with loop index i
        #   - if s[i] == substring[r], i increments, and r increments, and goes back to 0 if it equals len(substring)
        #   - if s[i] != substring[r], substring gets set to s[:i+1], r gets reset to 0
        # - when the loop exits, substring should equal the longest repeating substring, or s[:len(s)//2 + 1]
        #
        # actually, this runs into a problem! For cases like 'abacababacababacababacab', by the time my algorithm finds
        # that it needs to stop the substring, it's already well into the next copy of the valid substring. For the
        # example i provide, my algorithm finds 'abacababac', but the answer should be 'abacab'.
        #
        # so let's rethink. Can we just brute force it? we can loop from 1 to len(s)//2 + 1, indexed by i. if i divides
        # evenly into len(s), then we check if s[:i] * len(s)/(i) == s. This loop takes ~log(N) iterations (because it
        # skips iterations where i doesn't divide evenly into len(s)), and each iteration it performs an O(N) string
        # comparison, so it's O(NlogN)
        #
        # I'm not sure if there's a cleverer way of doing things...
        #
        # edit: turns out there is, we can check if s in (2*s)[1:-1], and that's it!
        # why "return s in (2*s)[1:-1]" works: checking (2*s)[1:-1] is like checking if s is equal to some rotation of
        # itself. This is O(N).

        # trivial case
        if len(s) < 2:
            return False

        for i in range(1, len(s)//2 + 1):
            if len(s) % i == 0:
                if s[:i] * (len(s)//i) == s:
                    return True

        return False
