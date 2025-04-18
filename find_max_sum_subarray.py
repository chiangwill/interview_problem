'''
Given an array of n positive integers, find a contiguous subarray (with length greater than one) such that the sum of the minimum and maximum elements in the subarray is maximized.

e.g. 4, 6, 2, 8, 10 -> Answer is 18

Follow up:
Given an array of integers nums, find indexes [i, j] such that the subarray sum nums[i] + nums[i+1] ... nums[j-1] + nums[j] is maximum and nums[i] is equal to nums[j]
'''

# def max_subarray_sum(array):

#     curr = res = 0

#     for num in array:
#         curr = max(0, curr + num)
#         res = max(res, curr)

#     return res


def max_sum_subarray(nums):

    n = len(nums)
    prefix_sum = []

    prefix = 0
    for num in nums:
        prefix_sum.append(prefix + num)
        prefix += num

    num_to_indices = {}
    for idx, num in enumerate(nums):
        if num not in num_to_indices:
            num_to_indices[num] = []

        num_to_indices[num].append(idx)

    max_sum = float('-inf')
    res = []

    for num, indices in num_to_indices.items():
        if len(indices) <= 1:
            continue

        for i in range(len(indices)):
            for j in range(i + 1, len(indices)):
                left_idx = indices[i]
                right_idx = indices[j]

                right_sum = prefix_sum[right_idx]
                left_sum = prefix_sum[left_idx - 1] if left_idx != 0 else 0

                curr_sum = right_sum - left_sum

                if curr_sum > max_sum:
                    max_sum = curr_sum
                    res = [left_idx, right_idx]

    return res


print(max_sum_subarray([1, 2, 3, 4, 2, 3]))
print(max_sum_subarray([1, 3, 5, 6, 3, -6, 3]))
# print(max_sum_subarray([2, 1, 2]))
