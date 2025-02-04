class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        res=nums[0]
        max1=nums[0]

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                max1+=nums[i]
            else:
                max1=nums[i]
            res=max(res,max1)
        return res

        

