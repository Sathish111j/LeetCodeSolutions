class Solution:
    def isPalindrome(self, x: int) -> bool:
        # numstr=str(x)
        # reversed=0

        # while l<=r:
        #     if numstr[l]!=numstr[r]:
        #         return False
        #     l+=1
        #     r-=1

        # return True


        if x< 0:
            return False
        
        reversedd=0
        temp=x
        while temp!=0:
            digit=temp%10
            reversedd = reversedd*10 + digit
            temp//=10
        return reversedd == x


