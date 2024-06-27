class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums)==1:
            return nums[0]
        
        prev2=0
        prev1=nums[0]

        for i in range(1,len(nums)):
            current = max(prev1, nums[i]+prev2)
            prev2=prev1
            prev1=current
        return prev1