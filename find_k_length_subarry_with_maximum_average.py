'''
Given an integer array nums and an integer k, find all contiguous subarrays of length k that have the maximum average value.
If there are multiple subarrays with the same maximum average value, return all of them.
'''


def find_maximum_subarray(nums, k):

    n = len(nums)
    left = 0
    max_sum = float('-inf')
    curr_sum = 0
    res = []

    for right in range(n):
        curr_sum += nums[right]

        if right - left + 1 == k:
            if curr_sum == max_sum:
                res.append(nums[left:right + 1])
                left += 1
            elif curr_sum > max_sum:
                res = []
                max_sum = curr_sum
                res.append(nums[left:right + 1])
                left += 1

            curr_sum -= nums[left]
            left += 1

    return res


print(find_maximum_subarray([1, 2, 3, 4, 5], 2))
print(find_maximum_subarray([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
