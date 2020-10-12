"""
LC49 - Group anagrams

49. Group Anagrams
Medium

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

------------------------------------------------------------------------------------------------------------------------

The idea here is to turn each word in the list into a representation of letter frequency. We do this by turning the word
into either a string or tuple (here, we use a string) with its letter frequencies, and then using that as a hash to add
the words to a dictionary, grouped by letter frequencies
"""


def get_hash_array(string):
    ret = [0] * 26

    for s in string:
        ret[ord(s) - ord('a')] += 1

    return str(ret)


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # sorting hash method
        #         out_dict = {}

        #         for s in strs:
        #             c = ''.join(sorted(s))
        #             if c not in out_dict:
        #                 out_dict[c] = [s]
        #             else:
        #                 out_dict[c].append(s)

        #         return [out_dict.values()]

        # array hash method
        out_dict = {}

        for s in strs:
            c = get_hash_array(s)
            if c not in out_dict:
                out_dict[c] = [s]
            else:
                out_dict[c].append(s)

        # apparently order does matter lol, it likes it to be in ascending order according to array size, and for each
        # array to be alphabetically sorted
        return sorted([sorted(v) for v in out_dict.values()], key=len)