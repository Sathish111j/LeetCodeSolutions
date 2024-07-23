class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        dp =[[0]*(target+1) for _ in range(n)]
        
        for i in range(n):
            dp[i][0]=True
        
        dp[0][nums[0]]=True
        
        for index in range(1,n):
            for tar in range(1,target+1):
                notTake=dp[index-1][tar]
                take=False

                if nums[index]<=tar:
                    take=dp[index-1][tar-nums[index]]

                    dp[index][tar]=take or notTake
        
        return dp[n-1][target]