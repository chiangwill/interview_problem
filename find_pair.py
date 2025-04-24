def find_pair(nums, k):

    last_idx = {}

    n = len(nums)

    for i in range(n):
        num = nums[i]

        if num in last_idx:
            prev_idx = last_idx[num]

            if i - prev_idx <= k:
                return True

        last_idx[num] = i

    return False


print(find_pair([1, 2, 3, 1], 3))
print(find_pair([1, 2, 3, 1, 2, 3], 2))
