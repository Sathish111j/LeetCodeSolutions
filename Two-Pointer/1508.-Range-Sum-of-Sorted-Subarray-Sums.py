class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int: 
        
        subarraySum = []
        n = len(nums)
        MOD = 10**9 + 7
        
        for start in range(n):
            for end in range(start, n):
                subarray = nums[start:end + 1]
                subarraySum.append(sum(subarray))

        subarraySum.sort()

        return sum(subarraySum[left-1:right])%MOD
            
          
        
