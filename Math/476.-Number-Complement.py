class Solution:
    def findComplement(self, num: int) -> int:
        i=0
        ans=0

        while num :
            temp=num&1
            if not temp :
                ans+= 2 **i
            num=num>>1
            i+=1
        return ans