class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1

        while l<r:
            if s[l]!=s[r]:
                skipRight,skipLeft=s[l+1:r+1],s[l:r]
                return skipRight==skipRight[::-1] or skipLeft==skipLeft[::-1] #check for palindrome when
                # the two pointer are not same skip any of those and check it

            l,r=l+1,r-1
        return True
        
            
        