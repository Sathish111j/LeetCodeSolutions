class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        if n == 1:
            return cost[0]
        if n == 2:
            return min(cost[0], cost[1])

        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(2, n):
            current = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = current
        return min(prev1, prev2)



        # cost.append(0)

        # for i in range(len(cost)-3,-1,-1):
        #     cost[i]+=min(cost[i+1],cost[i+2])

        # return min (cost[0],cost[1])



# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         dp = [0 for _ in range(len(cost)+1)]

#         #step 0 and 1 both cost 0
#         for i in range(2, len(cost)+1):
#             # we will take the lesser total cost between getting 
#             # here from one step down or two steps down
#             dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

#         # we care about the cost to get past the last step
#         return dp[len(cost)]