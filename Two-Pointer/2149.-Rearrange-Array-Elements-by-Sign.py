class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # p1 = 0
        # p2 = 1

        # while p1 < len(nums):
        #     if p1 % 2 == 0:
        #         if nums[p1] < 0:
        #             while p2 < len(nums) and nums[p2] < 0:
        #                 p2 += 1
                    
        #             if p2 < len(nums):
        #                 nums.insert(p1, nums.pop(p2))
        #                 if p2 < p1:
        #                     p1 += 1
        #     else:
        #         if nums[p1] > 0:
        #             while p2 < len(nums) and nums[p2] > 0:
        #                 p2 += 1
        #             if p2 < len(nums):
        #                 nums.insert(p1, nums.pop(p2))
        #                 if p2 < p1:
        #                     p1 += 1
        #     p1 += 1
        #     p2 = p1 + 1
            
        # return nums TLE

        n = len(nums)
        result = [0] * n
        posIndex, negIndex = 0, 1
        
        for num in nums:
            if num > 0:
                result[posIndex] = num
                posIndex += 2
            else:
                result[negIndex] = num
                negIndex += 2
        
        return result

