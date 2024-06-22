class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        hashmap={ s for s in nums}

        def backtrack(i,current):
            if i==len(nums):
                res="".join(current)
                if res in hashmap:
                    return None
                else:
                    return res
            res=backtrack(i+1,current)
            if res:
                return res


            current[i]="1"
            res=backtrack(i+1,current)

            if res:
                return res
            
            return None
        return backtrack(0, ['0'] * len(nums))
        