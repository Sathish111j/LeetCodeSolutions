class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset={}

        for i,n in enumerate(nums):
            dif=target-n
            if dif in hashset:
                return [hashset[dif],i]
            hashset[n]=i
        