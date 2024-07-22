class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # # cant solve this using greedy because there is no uniformity in the inputs and doesnt always give the required solution hence we need to try all possible combinations using backtracking and dp 
        # def coin (index,target):
        #     if index==0:
        #         if target % coins[index]==0:
        #             return target//coins[index]
        #         else:
        #             return float("inf")

        #     notTake=0+coin(index-1,target)
        #     take=float("inf")

        #     if coins[index]<=target:
        #         take = 1+ coin(index,target-coins[index]) # when there is thing calleld infifnte supply then we need to stand in same place to get all the supply till its needed

        #     return min(notTake,take)

        # result = coin(len(coins) - 1, amount)
        # return result if result != float("inf") else -1


        # memo method

        # memo={}
        # def coin (index,target):
        #     if (index,target) in memo:
        #         return memo[(index,target)]
        #     if index==0:
        #         if target % coins[index]==0:
        #             return target//coins[index]
        #         else:
        #             return float("inf")

        #     notTake=0+coin(index-1,target)
        #     take=float("inf")

        #     if coins[index]<=target:
        #         take = 1+ coin(index,target-coins[index]) # when there is thing calleld infifnte supply then we need to stand in same place to get all the supply till its needed
        #     memo[(index,target)]=min(notTake,take)
        #     return memo[(index,target)]

        # result = coin(len(coins) - 1, amount)
        # return result if result != float("inf") else -1

        #Tabulation

        # n = len(coins)
        # dp = [[float('inf')] * (amount + 1) for _ in range(n)]

        # for T in range(amount + 1):
        #     if T % coins[0] == 0:
        #         dp[0][T] = T // coins[0]
        #     else:
        #         dp[0][T] = float('inf')

        # for ind in range(1, n):
        #     for T in range(amount + 1):
        #         not_take = 0 + dp[ind - 1][T]
        #         take = float('inf')
        #         if coins[ind] <= T:
        #             take = 1 + dp[ind][T - coins[ind]]
        #         dp[ind][T] = min(take, not_take)

        # ans = dp[n - 1][amount]
        # return ans if ans != float('inf') else -1

        # Space Optimized

        n = len(coins)
        prev = [float('inf')] * (amount + 1)
        cur = [float('inf')] * (amount + 1)

        for T in range(amount + 1):
            if T % coins[0] == 0:
                prev[T] = T // coins[0]
            else:
                prev[T] = float('inf')

        for ind in range(1, n):
            for T in range(amount + 1):
                not_take = prev[T]
                take = float('inf')
                if coins[ind] <= T:
                    take = 1 + cur[T - coins[ind]]
                cur[T] = min(take, not_take)
            prev = cur[:]
        ans = prev[amount]
        return ans if ans != float('inf') else -1
                
            



            
            

