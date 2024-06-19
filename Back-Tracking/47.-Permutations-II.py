class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result=[]
        permutation=[]
        count={n:0 for n in nums}

        for n in nums:
            count[n]+=1
        
        def dfs():

            if len(permutation)==len(nums):
                result.append(permutation.copy())
                return
            
            for n in count:
                if count[n]>0:
                    permutation.append(n)
                    count[n]-=1

                    dfs()

                    permutation.pop()
                    count[n]+=1
        dfs()
        return result
