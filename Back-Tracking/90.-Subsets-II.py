class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #same as creating noraml subset but need to skip duplicates
        result = []
        nums.sort()
        def recursive(i, subset):
            if i == len(nums):
                result.append(subset.copy())
                return
                
            # include nums[i] in the subset
            subset.append(nums[i])
            recursive(i + 1, subset)

            # exclude nums[i] from the subset
            subset.pop()
            #skiping duplicate
            while i+1 < len(nums) and nums[i]==nums[i+1]:
                i+=1
            recursive(i + 1, subset)
        
        recursive(0, [])
        return result
