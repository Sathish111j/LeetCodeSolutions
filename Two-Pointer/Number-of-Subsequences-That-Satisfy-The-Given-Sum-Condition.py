class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        result=0
        modulo=10**9+7
        right=len(nums)-1

        for i, left in enumerate(nums):
            while (left + nums[right]) > target and i<=right:
                right-=1
            if i<=right:
                result += (2**(right-i)) 
                result%=modulo
        return result
