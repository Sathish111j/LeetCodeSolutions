class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # lengthInc=1
        # lengthDesc=1
        # l1=0
        # l2=0

        # for r in range(1,len(nums)):
        #     if  nums[r]>nums[r-1]:
        #         lengthInc=max(lengthInc,r-l1+1)
        #     else:
        #         l1=r
        #     if  nums[r]<nums[r-1]:
        #         lengthDesc=max(lengthDesc,r-l2+1)
        #     else:
        #         l2=r
        
        # return max(lengthInc,lengthDesc)
            
        inc = dec = max_len = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = dec = 1

            max_len = max(max_len, inc, dec)

        return max_len


