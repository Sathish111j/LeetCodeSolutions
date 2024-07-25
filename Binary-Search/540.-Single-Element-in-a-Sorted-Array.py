class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low,high=0,len(nums)-1

        while low<high:
            mid=low + (high-low)//2
            
            if mid%2==1:
                mid-=1
            
            if nums[mid]!=nums[mid+1]:
                high=mid
            else:
                low=mid+2
            
        return nums[high]

            