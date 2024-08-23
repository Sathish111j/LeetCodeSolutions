class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        l=0
        nums.sort()
        windowSum=0
        maxlength=0

        for r in range(len(nums)):
            windowSum+=nums[r]
            
            if k<nums[r]*(r-l+1) -windowSum:
                windowSum-=nums[l]
                l+=1

            maxlength=max(maxlength,r-l+1)

        return maxlength
            