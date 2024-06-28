class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        max_length = 0
        zeros_count = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                zeros_count += 1

            if zeros_count > k:
                if nums[l] == 0:
                    zeros_count -= 1
                l += 1

            max_length = max(max_length, end - l + 1)

        return max_length
                
            