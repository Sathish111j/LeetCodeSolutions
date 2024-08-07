# Given an array arr, partition it into two subsets(possibly empty) such that each element must belong to only one subset. Let the sum of the elements of these two subsets be S1 and S2. 
# Given a difference d, count the number of partitions in which S1 is greater than or equal to S2 and the difference between S1 and S2 is equal to d. Since the answer may be large return it modulo 109 + 7.

# Example 1:

# Input:
# n = 4
# d = 3
# arr[] =  { 5, 2, 6, 4}
# Output: 1
# Explanation:
# There is only one possible partition of this array. Partition : {6, 4}, {5, 2}. The subset difference between subset sum is: (6 + 4) - (5 + 2) = 3.


mod=int(1e9+7)
def findWays(num, tar):
    n = len(num)
    dp = [[0] * (tar + 1) for _ in range(n)]
    
    if num[0] == 0:
        dp[0][0] = 2 # 2 cases - pick and not pick
    else:
        dp[0][0] = 1 # 1 case - not pick
    
    if num[0] != 0 and num[0] <= tar:
        dp[0][num[0]] = 1 # 1 case - pick
    
    for ind in range(1, n):
        for target in range(tar + 1):
            notTaken = dp[ind - 1][target]
            taken = 0
            if num[ind] <= target:
                taken = dp[ind - 1][target - num[ind]]
        
            dp[ind][target] = (notTaken + taken) % mod
    return dp[n - 1][tar]

def countPartitions(n, d, arr):
    totSum = sum(arr)
    
    # Checking for edge cases
    if (totSum - d) < 0 or (totSum - d) % 2:
        return 0
    
    return findWays(arr, (totSum - d) // 2)