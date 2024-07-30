class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        numsSum=sum(nums)

        for i in range(len(nums)-1,1,-1):
            numsSum-=nums[i]
            if numsSum>nums[i]:
                return numsSum+nums[i]
        
        return -1

