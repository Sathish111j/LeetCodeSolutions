class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = 0
        modulo = 10**9 + 7

        for i, left in enumerate(nums):
            right = len(nums) - 1  # reset right pointer for each left pointer
            while left + nums[right] > target and i <= right:
                right -= 1
            if i <= right:
                result += pow(2, right - i, modulo)
                result %= modulo
        return result
