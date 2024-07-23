class Solution:
    def change(self, T: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1 for _ in range(T + 1)] for i in range(n)]
    
        for t in range(T + 1):
            if t % coins[0] == 0:
                dp[0][t] = 1
            else:
                dp[0][t] = 0

        for ind in range(1, n):
            for target in range(T + 1):
                notTaken = dp[ind - 1][target] 
                taken = 0
                if coins[ind] <= target:
                    taken = dp[ind][target - coins[ind]]
                dp[ind][target] = notTaken + taken
        return dp[n - 1][T]
            