class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result=0
        l=0
        charset=set()

        for r in range (len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            result=max(r-l+1,result)
        return result
