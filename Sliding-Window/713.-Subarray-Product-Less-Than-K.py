class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l=0
        total=0
        prd = 1

        for r in range(len(nums)):
            prd*= nums[r]

            while prd>=k and l<=r:
                prd//=nums[l]
                l+=1
            total+=r-l+1 # here this done because it add the window size because the window itself and the elemts combos inside the window are also sperately lees than k 
        
        
            
        return total

