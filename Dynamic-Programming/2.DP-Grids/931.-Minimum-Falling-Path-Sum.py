class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        dp=[[-1]*n for _ in range(n)]

        for i in range (n):
            for j in range(n):
                if i ==0:
                    dp[i][j]=matrix[i][j] # initilizing the dp can be done outside also
                else:
                    up = matrix[i][j] + dp[i-1][j]
                    ld = matrix[i][j] + dp[i-1][j-1] if j-1 >= 0 else float("inf")
                    rd = matrix[i][j] + dp[i-1][j+1] if j+1 < n else float("inf")
                    dp[i][j] = min(up, ld, rd)

        maxi=float("inf")
        for i in range(n):
            maxi=min(maxi,dp[n-1][i])

        return maxi        

