def valid_path(grid):
    '''
    DFS + visited
    time complexity: O(m * n)
    space complexity: O(m * n) (modify the original grid can optimization to O(1))

    Tortoise and Hare Algorithm
    time complexity: O(m * n)
    space complexity: O(1)
    '''

    m, n = len(grid), len(grid[0])

    def next_cell(row, col):

        if row < 0 or row >= m or col < 0 or col >= n:
            return (-1, -1)

        direction = grid[row][col]

        if direction == 'R' and col + 1 < n:
            return (row, col + 1)
        elif direction == 'L' and col - 1 >= 0:
            return (row, col - 1)
        elif direction == 'U' and row - 1 >= 0:
            return (row - 1, col)
        elif direction == 'D' and row + 1 < m:
            return (row + 1, col)
        else:
            return (-1, -1)

    slow_row, slow_col = 0, 0
    fast_row, fast_col = 0, 0

    while True:

        slow_row, slow_col = next_cell(slow_row, slow_col)
        if (slow_row, slow_col) == (-1, -1):
            return False

        for _ in range(2):
            fast_row, fast_col = next_cell(fast_row, fast_col)
            print((fast_row, fast_col))

            if (fast_row, fast_col) == (m - 1, n - 1):
                return True

            if (fast_row, fast_col) == (-1, -1):
                return False

        if (slow_row, slow_col) == (fast_row, fast_col):
            return False

    # m, n = len(grid), len(grid[0])

    # visited = set()

    # def dfs(row, col):
    #     if row == m - 1 and col == n - 1:
    #         return True

    #     if row < 0 or row >= m or col < 0 or col >= n:
    #         return False

    #     if (row, col) in visited:
    #         return False

    #     direction = grid[row][col]
    #     visited.add((row, col))

    #     if direction == 'R':
    #         return dfs(row, col + 1)
    #     elif direction == 'L':
    #         return dfs(row, col - 1)
    #     elif direction == 'D':
    #         return dfs(row + 1, col)
    #     else:
    #         return dfs(row - 1, col)

    # return dfs(0, 0)


print(valid_path([['R', 'R', 'D'], ['D', 'L', 'D'], ['R', 'R', 'X']]))
# print(valid_path([['R', 'D', 'R'], ['U', 'L', 'D'], ['R', 'R', 'X']]))
