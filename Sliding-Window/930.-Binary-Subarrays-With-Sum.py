class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def atMost(g):
            if g < 0:
                return 0
            count = left = curr_sum = 0
            for right in range(len(nums)):
                curr_sum += nums[right]
                while curr_sum > g:
                    curr_sum -= nums[left]
                    left += 1
                count += right - left + 1
            return count

        return atMost(goal) - atMost(goal - 1)

# atMost(goal)` gives  the count of subarrays with sum <= goal
# atMost(goal - 1)` gives us the count of subarrays with sum < goal
# The difference is exactly the count of subarrays with sum equal to goal