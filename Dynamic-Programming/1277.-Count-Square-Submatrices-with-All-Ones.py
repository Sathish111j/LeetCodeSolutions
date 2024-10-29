class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i == 0 or j == 0:
                        dp[i][j] = matrix[i][j]
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                res += dp[i][j]
                
        return res