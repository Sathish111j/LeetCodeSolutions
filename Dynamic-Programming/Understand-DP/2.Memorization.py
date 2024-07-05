def solve(ind, height, dp):
    if ind == 0:
        return 0
    if dp[ind] != -1:
        return dp[ind]
    
    jumpOne = solve(ind - 1, height, dp) + abs(height[ind] - height[ind - 1])
    jumpTwo =float('inf')
    if ind > 1:
        jumpTwo = solve(ind - 2, height, dp) + abs(height[ind] - height[ind - 2])
    
    dp[ind] = min(jumpOne, jumpTwo)
    return dp[ind]
