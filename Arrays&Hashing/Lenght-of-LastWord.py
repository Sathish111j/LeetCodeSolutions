class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length=0
        spacelenght=0
        for i in range(len(s)):
            if (s[i]!=" "):
                length+=1
                lastword=length
            else:
                length=0
        return lastword
        
        