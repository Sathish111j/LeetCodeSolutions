class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def recursive(i, subset):
            if i == len(nums):
                result.append(subset.copy())
                return
                
            # include nums[i] in the subset
            subset.append(nums[i])
            recursive(i + 1, subset)

            # exclude nums[i] from the subset
            subset.pop()
            recursive(i + 1, subset)
        
        recursive(0, [])
        return result
