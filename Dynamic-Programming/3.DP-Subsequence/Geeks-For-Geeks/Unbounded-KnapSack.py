def unboundedKnapsack(n, W, val, wt):
    dp = [[0 for _ in range(W + 1)] for _ in range(n)]

    for W in range(W + 1):
        dp[0][W] = (W // wt[0]) * val[0]

    for ind in range(1, n):
        for W in range(W + 1):
            notTake = dp[ind - 1][W]
            take = 0
            if wt[ind] <= W:
                take = val[ind] + dp[ind][W - wt[ind]]
            dp[ind][W] = max(take, notTake)

    return dp[n - 1][W]


def unboundedKnapsack(n, W, val, wt):
    prev = [0] * (W + 1)
    curr = [0] * (W + 1)

    for w in range(W + 1):
        prev[w] = (w // wt[0]) * val[0]

    for ind in range(1, n):
        for w in range(W + 1):
            notTake = prev[w]
            take = 0
            if wt[ind] <= w:
                take = val[ind] + curr[w - wt[ind]]
            curr[w] = max(take, notTake)
        prev, curr = curr, prev  # Swap references for the next iteration

    return prev[W]

def unboundedKnapsack(n, W, val, wt):
    prev = [0] * (W + 1)

    for w in range(W + 1):
        prev[w] = (w // wt[0]) * val[0]

    for ind in range(1, n):
        for w in range(W + 1):
            notTake = prev[w]
            take = 0
            if wt[ind] <= w:
                take = val[ind] + prev[w - wt[ind]]
            prev[w] = max(take, notTake)

    return prev[W]
