def get_smallest_subarray(nums):

    n = len(nums)

    if n < 2:
        return [-1, -1]

    end = -1
    curr_max_from_left = nums[0]

    for i in range(1, n):
        if nums[i] < curr_max_from_left:
            end = i
        curr_max_from_left = max(curr_max_from_left, nums[i])

    if end == -1:
        return [-1, -1]

    start = -1
    curr_min_from_right = nums[n - 1]

    for i in range(n - 2, -1, -1):
        if nums[i] > curr_min_from_right:
            start = i
        curr_min_from_right = min(curr_min_from_right, nums[i])

    return [start, end]


print(get_smallest_subarray([7, 10, 15, 25, 40, 20, 31, 32, 70, 100]))
print(get_smallest_subarray([4, 3, 2, 1]))
print(get_smallest_subarray([1, 2, 4, 5, 6, 8, 12, 11, 20]))
print(get_smallest_subarray([10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]))
