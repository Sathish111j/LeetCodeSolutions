class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        longest=0

        for n in numset:
            if n-1 not in numset:
                long=0
                while(n+long) in numset:
                    long+=1
                longest=max(long,longest)
        return longest
            