"""
LC406 - Queue Reconstruction by Height

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k),
where h is the height of the person and k is the number of people in front of this person who have a height greater than
or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


--------------------------------------------

Two solutions.
person = [p, q]
1. When sorted in increasing order by height (p), q is the number of blanks or people of greater or equal height in
front of person in the array. Can insert this way, but this is less efficient
2. When sorted in decreasing order by height (p) and subsorted increasing order by q, persons can be inserted in order,
where q is the actual index, starting with an empty list. can use python's list.insert method for this

"""


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        # first attempt: sort height in ascending order, insert based on number of blanks or geq heights in front
        # after sorting people by height, we process each person in order. Since heights are in order,
        # each person [p, q] must leave exactly q blank spaces in front of itself

        #         ps = sorted(people, key=lambda x: x[0])  # O(NlogN)
        #         out = [[] for _ in range(len(people))]

        #         for p in ps:
        #             c = p[1]

        #             for i in range(len(out)):
        #                 if c == 0 and not out[i]:
        #                     out[i] = p
        #                     break
        #                 else:
        #                     if not out[i]:
        #                         c -= 1
        #                     elif out[i][0] >= p[0]:
        #                         c -= 1

        #         return out

        # second attempt: sort in descending order by height, ascending order by number of people, insert
        # into correct position. We note that, in descending order of height and ascending order of number of people
        # in front, the number of people in front is the correct index in the list at the time of insertion
        out = []
        for p in sorted(people, key=lambda x: (-x[0], x[1])):
            out.insert(p[1], p)
        return out