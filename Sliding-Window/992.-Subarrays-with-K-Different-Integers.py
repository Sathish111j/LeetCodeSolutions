class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(K):
            l, r = 0, 0
            cnt = 0
            mpp = defaultdict(int)
            
            while r < len(nums):
                mpp[nums[r]] += 1
                
                while len(mpp) > K:
                    mpp[nums[l]] -= 1
                    if mpp[nums[l]] == 0:
                        del mpp[nums[l]]
                    l += 1
                
                cnt += r - l + 1
                r += 1
            
            return cnt
        
        return atMostK(k) - atMostK(k - 1)