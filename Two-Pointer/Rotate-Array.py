class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)

        l,r=0,len(nums)-1
        while l<r: #reverse the array completely by swaping
            nums[l],nums[r]=nums[r],nums[l]
            l,r=l+1,r-1
        
        l,r=0,k-1
        while l<r: # reverse the first k elements
            nums[l],nums[r]=nums[r],nums[l]
            l,r=l+1,r-1
        
        l,r=k,len(nums)-1
        while l<r: #reverse the other than first k elements
            nums[l],nums[r]=nums[r],nums[l]
            l,r=l+1,r-1

        