class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # for this we need to ensure that the both the neighbour are greater that it or less than it
        # so sort it and add one from left and one from right

        nums.sort()
        result=[]

        l,r=0,len(nums)-1

        while len(result)!=len(nums):
            result.append(nums[l])
            l+=1

            if l<=r:
                result.append(nums[r])
                r-=1
        return result