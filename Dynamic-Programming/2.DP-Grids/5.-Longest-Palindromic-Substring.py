class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res=""

        def helper(l,r):
            while l>=0 and r <len(s) and s[l]==s[r]:
                if r-l+1 > len(self.res):
                    self.res=s[l:r+1]
                l-=1
                r+=1


        for i in range(len(s)):
            helper(i,i) # for odd length
            helper(i,i+1) # for even length

        return self.res