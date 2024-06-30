class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(g):
            if g < 0:
                return 0
            count = left = curr_sum = 0
            for right in range(len(nums)):
                curr_sum += nums[right] % 2
                while curr_sum > g:
                    curr_sum -= nums[left] % 2 
                    left += 1
                count += right - left + 1
            return count

        return atMost(k) - atMost(k - 1)