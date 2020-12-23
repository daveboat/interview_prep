"""
LC239 - Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the
array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one
position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:

Input: nums = [1], k = 1
Output: [1]

Example 3:

Input: nums = [1,-1], k = 1
Output: [1,-1]

Example 4:

Input: nums = [9,11], k = 2
Output: [11]

Example 5:

Input: nums = [4,-2], k = 2
Output: [4]

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    1 <= k <= nums.length
"""
from collections import deque


class Solution(object):
    #     def initialize_window(self, window):
    #         # return the maximum and index of that maximum. In the case of a tie, return the maximum with the
    #         # largest index. O(k).

    #         max_val = window[0]
    #         max_ind = 0
    #         for i in range(len(window)):
    #             if window[i] >= max_val:
    #                 max_val = window[i]
    #                 max_ind = i

    #         return max_val, max_ind

    #     def maxSlidingWindow(self, nums, k):
    #         """
    #         :type nums: List[int]
    #         :type k: int
    #         :rtype: List[int]
    #         """
    #         # the brute force way is to just do the sliding window and find a max each time. Could we do better?
    #         # how about using a heap? Doesn't really work because we need to remove some arbitrary element
    #         # each time we move the window.
    #         # how about using a dictionary, like with strings? It's possible, but since your numbers are
    #         # not restricted, you're doing an O(N) space O(N) time operation every time anyways
    #         # if we use a queue, is there a way to do better than O(Nk) in time and O(k) in space?
    #         #
    #         # let's think about this carefully. We start with N numbers and a k-length window. We initialize
    #         # a queue with the first k elements, and do an O(k) max operation to find the current maximum.
    #         # Let's try the following. To initialize, we not only find the value of the maximum, but also its
    #         # position. When we advance, the position decreases by 1 if a new or equal maximum isn't added at the
    #         # head of the queue. If a new or equal maximum is added to the head of the queue, we reset the
    #         # maximum index to k-1. If the maximum index gets decremented to -1, (in other words, it leaves the
    #         # window), and a new or equal max was never found in the meantime, we need to re-initialize to
    #         # find a new max value and index
    #         #
    #         # This way, we are O(k) space, and O(N) + O(N/k) in time on average. In the worst case scenario where
    #         # nums is strictly monotonically decreasing, we do terribly though, with O(Nk) time

    #         # initialize window
    #         window = [0] * k
    #         window[:] = nums[:k]
    #         max_val, max_ind = self.initialize_window(window)
    #         ret = [max_val]

    #         for num in nums[k:]:
    #             # do queue adjustment
    #             window.append(num)
    #             window.pop(0)

    #             # check new number against max
    #             if num >= max_val:  # if the newly appended value is larger or equal, reset max_ind and max_val
    #                 max_val, max_ind = num, k - 1
    #             else:  # else decrement max_ind and check that it hasn't left the queue
    #                 max_ind -= 1
    #                 # if the former max has left the queue, re-initialize
    #                 if max_ind < 0:
    #                     max_val, max_ind = self.initialize_window(window)

    #             # add the current max_val to the return list
    #             ret.append(max_val)

    #         return ret

    # I included my attempt, but the best solution uses a monotonic queue. Not my code:
    def maxSlidingWindow(self, nums, k):
        deq, n, ans = deque([0]), len(nums), []

        for i in range(n):
            while deq and deq[0] <= i - k:
                deq.popleft()
            while deq and nums[i] >= nums[deq[-1]]:
                deq.pop()
            deq.append(i)

            ans.append(nums[deq[0]])

        return ans[k - 1:]
