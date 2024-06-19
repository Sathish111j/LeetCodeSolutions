class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]

        if len(nums)==1:
            return [nums.copy()]
        
        for i in range(len(nums)):
            n=nums.pop(0)
            perms=self.permute(nums)

            for perm in perms:
                perm.append(n)
            # put back the first element at last, so now 2nd element will be first 
            # and will be considered in the next iteration
            result.extend(perms)
            nums.append(n)
        return result