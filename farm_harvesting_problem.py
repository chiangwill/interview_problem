def farm_harvesting(grid, k):
    '''

        農場採收問題 (Farm Harvesting Problem)

        想像你有一個 m x n 的農場，表示為一個二維陣列 grid，其中 grid[i][j] 代表第 i 行第 j 列這塊土地的作物產量 (一個非負整數)。

        你從農場的左上角 (0, 0) 出發，目標是走到右下角 (m-1, n-1)。你每次只能往右或下移動。

        特別的是，你攜帶的籃子容量有限，沿途你最多只能選擇 k 塊土地進行採收。也就是說，在你從 (0, 0) 到 (m-1, n-1) 的路徑上，你可以選擇經過的土地中，最多 k 塊地來採集其產量。如果你經過一塊土地但選擇不採收，則該土地的產量對你來說就是 0。

        你的任務是找出從 (0, 0) 到 (m-1, n-1) 的所有可能路徑中，遵循上述規則 (只能往下或往右，最多採收 k 塊地) 的情況下，能獲得的最大總產量是多少？

        '''

    m, n = len(grid), len(grid[0])
    dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]
    dp[0][0][0] = 0

    if k >= 1:
        dp[0][0][1] = grid[0][0]

    for i in range(m):
        for j in range(n):
            for c in range(k + 1):
                if i > 0:
                    # 情況 A: 到 (i-1, j) 已收 c 塊，到 (i, j) 不收
                    if dp[i - 1][j][c] != -1:
                        dp[i][j][c] = max(dp[i][j][c], dp[i - 1][j][c])

                    # 情況 B: 到 (i-1, j) 已收 c-1 塊，到 (i, j) 收穫 (需 c > 0)
                    if c > 0 and dp[i - 1][j][c - 1] != -1:
                        dp[i][j][c] = max(dp[i][j][c], dp[i - 1][j][c - 1] + grid[i][j])

                if j > 0:
                    # 情況 C: 到 (i, j-1) 已收 c 塊，到 (i, j) 不收
                    if dp[i][j - 1][c] != -1:
                        dp[i][j][c] = max(dp[i][j][c], dp[i][j - 1][c])

                    # 情況 D: 到 (i, j-1) 已收 c-1 塊，到 (i, j) 收穫 (需 c > 0)
                    if c > 0 and dp[i][j - 1][c - 1] != -1:
                        dp[i][j][c] = max(dp[i][j][c], dp[i][j - 1][c - 1] + grid[i][j])

    final_max_yield = 0
    for c in range(k + 1):
        final_max_yield = max(final_max_yield, dp[m - 1][n - 1][c])

    return final_max_yield if final_max_yield != -1 else 0  # 如果終點不可達，返回 0


print(farm_harvesting([[1, 10], [5, 8]], 1))
