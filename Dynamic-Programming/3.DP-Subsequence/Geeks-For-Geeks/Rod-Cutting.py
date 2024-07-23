def rodCuttingRecursive(ind, N, prices):
    if ind == 0:
        return N * prices[0]
    notTake = rodCuttingRecursive(ind - 1, N, prices)
    take = float('-inf')
    rodLength = ind + 1
    if rodLength <= N:
        take = prices[ind] + rodCuttingRecursive(ind, N - rodLength, prices)
    return max(take, notTake)



def rodCuttingMemoization(ind, N, prices, dp):
    if ind == 0:
        return N * prices[0]
    if dp[ind][N] != -1:
        return dp[ind][N]
    
    notTake = rodCuttingMemoization(ind - 1, N, prices, dp)
    take = float('-inf')
    rodLength = ind + 1
    if rodLength <= N:
        take = prices[ind] + rodCuttingMemoization(ind, N - rodLength, prices, dp)
    
    dp[ind][N] = max(take, notTake)
    return dp[ind][N]

def rodCutting(prices, N):
    dp = [[-1 for _ in range(N + 1)] for _ in range(len(prices))]
    return rodCuttingMemoization(len(prices) - 1, N, prices, dp)



def rodCuttingTabulation(prices, N):
    dp = [[0 for _ in range(N + 1)] for _ in range(len(prices))]
    
    for n in range(N + 1):
        dp[0][n] = n * prices[0]
    
    for ind in range(1, len(prices)):
        for n in range(N + 1):
            notTake = dp[ind - 1][n]
            take = float('-inf')
            rodLength = ind + 1
            if rodLength <= n:
                take = prices[ind] + dp[ind][n - rodLength]
            dp[ind][n] = max(take, notTake)
    
    return dp[-1][-1]


def rodCuttingPrevCurr(prices, N):
    prev = [0] * (N + 1)
    curr = [0] * (N + 1)
    
    for n in range(N + 1):
        prev[n] = n * prices[0]
    
    for ind in range(1, len(prices)):
        for n in range(N + 1):
            notTake = prev[n]
            take = float('-inf')
            rodLength = ind + 1
            if rodLength <= n:
                take = prices[ind] + curr[n - rodLength]
            curr[n] = max(take, notTake)
        prev, curr = curr, prev
    
    return prev[N]


def rodCuttingSingleArray(prices, N):
    dp = [0] * (N + 1)
    
    for n in range(N + 1):
        dp[n] = n * prices[0]
    
    for ind in range(1, len(prices)):
        for n in range(N + 1):
            notTake = dp[n]
            take = float('-inf')
            rodLength = ind + 1
            if rodLength <= n:
                take = prices[ind] + dp[n - rodLength]
            dp[n] = max(notTake, take)
    
    return dp[N]
