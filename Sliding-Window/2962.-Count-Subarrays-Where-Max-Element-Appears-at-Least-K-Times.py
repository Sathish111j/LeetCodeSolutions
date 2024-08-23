class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxEle=max(nums)

        l=0
        total=0
        count=0

        for r in range(len(nums)):
            if nums[r]==maxEle:
                count+=1
            while count == k:
                if nums[l] == maxEle:
                    count -= 1
                l += 1
                
            total+=l # it will be 0 till it finds a subarray of the condition
        return total
                

                    