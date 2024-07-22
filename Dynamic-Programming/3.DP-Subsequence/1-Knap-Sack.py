def knapsack_tabulation(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):  
        for w in range(capacity + 1): 
            item_weight = weights[i - 1]
            item_value = values[i - 1]
            
            if item_weight > w:
                dp[i][w] = dp[i - 1][w]
            else:
                not_taken_value = dp[i - 1][w]
                taken_value = item_value + dp[i - 1][w - item_weight]
                dp[i][w] = max(not_taken_value, taken_value)
    return dp[n][capacity]
