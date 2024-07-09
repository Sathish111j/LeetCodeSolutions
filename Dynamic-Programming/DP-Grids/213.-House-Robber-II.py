class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        if len(nums)==1:
            return nums[0]
        
        def helper(nums):
            prev2=0
            prev1=0

            for num in nums:
                current = max(prev1, num+prev2)
                prev2=prev1
                prev1=current
            return prev1

        return max(helper(nums[1:]),helper(nums[:-1]))