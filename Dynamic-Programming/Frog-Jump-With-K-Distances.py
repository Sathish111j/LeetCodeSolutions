def solve_util(n, height, dp, k):
    dp[0] = 0
    for i in range(1, n):
        mmSteps = sys.maxsize  
        for j in range(1, k+1):
            if i - j >= 0:
                jump = dp[i - j] + abs(height[i] - height[i - j])
                mmSteps = min(jump, mmSteps) 
        dp[i] = mmSteps 

    return dp[n-1]