def count_subsets(arr, n, sum):
    MOD = 10**9 + 7
    dp = [[0] * (sum + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = 1
    
    for i in range(1, n + 1):
        current_element = arr[i - 1]
        for j in range(sum + 1):
            exclude_current = dp[i - 1][j]
            include_current = dp[i - 1][j - current_element] if j >= current_element else 0
            dp[i][j] = (exclude_current + include_current) % MOD
    
    return dp[n][sum]