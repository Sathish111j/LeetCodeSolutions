class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n=len(nums)
        totalOnes=sum(nums)

        if totalOnes==0 or totalOnes==n:
            return 0
        
        currentOnes=sum(nums[:totalOnes])
        maxOnes=currentOnes

        for i in range(n):
            currentOnes-=nums[i]
            currentOnes+=nums[(i+totalOnes)%n]
            maxOnes=max(maxOnes,currentOnes)
        
        return totalOnes-maxOnes