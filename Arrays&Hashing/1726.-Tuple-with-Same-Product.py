class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product=defaultdict(int)
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                prd=nums[i]*nums[j]
                count+=product[prd]*8
                product[prd]+=1

        return count                 
