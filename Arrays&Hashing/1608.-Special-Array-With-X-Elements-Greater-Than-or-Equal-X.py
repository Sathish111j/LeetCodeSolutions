class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        
        for i in range(len(nums)):
            count = len(nums) - i
            if nums[i] >= count:
                if i == 0 or nums[i - 1] < count:
                    return count
        
        return -1
