class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        sum1=sum(nums)
        n=len(nums)
        sum2=n*(n+1)//2

        return sum2 - sum1