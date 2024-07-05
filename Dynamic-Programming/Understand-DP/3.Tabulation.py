def solve(height):
    n = len(height)
    dp = [-1 for _ in range(n)]
    dp[0] = 0
    for ind in range(1, n):
        jumpOne = dp[ind - 1] + abs(height[ind] - height[ind - 1])
        jumpTwo = float('inf')
        if ind > 1:
            jumpTwo = dp[ind - 2] + abs(height[ind] - height[ind - 2])
        dp[ind] = min(jumpOne, jumpTwo)
    return dp[n - 1]
