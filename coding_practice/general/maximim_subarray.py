"""
LC53 - Maximum subarray

Return the largest sum of contiguous subarrays from an array.

Example, for [-2,1,-3,4,-1,2,1,-5,4], the result is 4-1+2+1 = 6

We use our own algorithm, which is actually just a mild variation of Kadane's algorithm
"""


def maximum_subarray(nums):
    # loop through the list

    l = len(nums)
    i = 0

    # keep track of largest and current sum
    largest_sum = 0
    current_sum = 0
    while i < l:

        current_sum += nums[i]

        if i == 0:  # need to do this for the special case where the list only contains negative values, eg nums = [-1]
            largest_sum = current_sum
        else:
            if current_sum > largest_sum:
                largest_sum = current_sum

        if current_sum < 0:
            current_sum = 0

        # increment counter
        i += 1

    return largest_sum


if __name__ == '__main__':
    print(maximum_subarray([-2]))