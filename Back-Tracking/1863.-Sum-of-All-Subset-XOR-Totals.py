class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def recursive(i, total):
            if i==len(nums):
                return total
            included=recursive(i+1, total^nums[i])
            excluded=recursive(i+1, total)

            return included +excluded
        return  recursive(0,0)