def get_min_subarry_square(nums, k):

    n = len(nums)

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, len(prefix) + 1):
        for j in range(1, k):
            dp[i][j]


print(get_min_subarry_square([1, 2, 3, 4, 5], 2))
