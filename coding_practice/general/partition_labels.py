"""
LC763 - Partition labels

A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so
that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:

    S will have length in range [1, 500].
    S will consist of lowercase English letters ('a' to 'z') only.
"""


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # the key thing to remember is that we want as many partitions as possible.
        # let's do this greedily?
        # - start with the first letter. find the last occurance of that letter. That's our proto-partition.
        # - for each other letter between the starting and ending positions, find the last position of that
        # letter in the string. If it's past the current last position, update the last position. We can
        # remember the last positions of all letters visited so we don't need to look for last positions
        # repeatedly.
        # - once we reach the last position, add S[start:last+1] to the output, and update start to last + 1
        # - if the last position ever gets updated to the length of S,  put S[start:end] into the output
        # and we're done
        #
        # we can use S.rfind() to find the last occurence of a character in the string
        #
        # edit: accepted, 80%

        last = dict()

        idx = 0
        end_index = 0
        start_index = 0

        # our return value
        partitions = []

        while idx < len(S):
            c = S[idx]

            # save last occurence of the current character in the string if it's not already saved
            if c not in last:
                last[c] = S.rfind(c)

            # if the final occurence of the character is greater than our current end_index, then update end_index
            if last[c] > end_index:
                end_index = last[c]

            # check to see if idx is at end_index. if so, set start_index and end_index to idx + 1
            if idx == end_index:
                partitions.append(end_index + 1 - start_index)
                start_index = idx + 1
                end_index = idx + 1

            # increment idx
            idx += 1

        return partitions
