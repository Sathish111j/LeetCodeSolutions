class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequency=Counter(nums)

        HighFrequency=max( frequency.values())

        return sum(count for element, count in frequency.items() if count == HighFrequency)