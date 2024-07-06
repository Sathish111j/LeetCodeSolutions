class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[[-1]*n for _ in range(n)]

        for j in range (n):
            dp[n-1][j]=triangle[n-1][j]

        for i in range(n-2,-1,-1):
            for j in range(i,-1,-1):
                d=triangle[i][j]+dp[i+1][j]
                dg=triangle[i][j]+dp[i+1][j+1]
                dp[i][j]=min(d,dg)
        return dp[0][0]

        # for i in range(len(triangle) - 2, -1, -1) :
        #     for j in range(i + 1) :
        #         triangle [i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        # return triangle[0][0]