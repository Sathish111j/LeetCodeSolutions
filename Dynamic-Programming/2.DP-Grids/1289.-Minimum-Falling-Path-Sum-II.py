class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # def backtrack(grid, i, j, n, dp):
        #     if i == n - 1:
        #         return grid[i][j]
        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     minPathSum = float('inf')
        #     for k in range(n):
        #         if k != j:
        #            minPathSum = min(minPathSum, grid[i][j] + backtrack(grid, i + 1, k, n, dp))
        #     dp[i][j] =minPathSum
        #     return dp[i][j]

        # n = len(grid)
        # dp = [[-1 for _ in range(n)] for _ in range(n)]
        # minPathSum = float('inf')
        # for j in range(n):
        #    minPathSum = min(minPathSum, backtrack(grid, 0, j, n, dp))
        # return minPathSum


        n = len(grid)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for j in range(n):
            dp[n-1][j] = grid[n-1][j]

        for i in range(n-2, -1, -1):
            for j in range(n):
                minPathSum = float('inf')
                for k in range(n):
                    if k != j:
                        minPathSum = min(minPathSum, grid[i][j] + dp[i + 1][k])
                dp[i][j] = minPathSum

        return min(dp[0])