class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        def count(n):
            return bin(n).count("1")
        
        currMin,currMax=nums[0],nums[0]
        prevMax=float("-inf")
        for n in nums:
            if count(n)==count(currMin):
                currMin=min(currMin,n)
                currMax=max(currMax,n)
            else:
                if currMin<prevMax:
                    return False
                prevMax=currMax
                currMin,currMax=n,n

        if currMin<prevMax:
            return False
        return True