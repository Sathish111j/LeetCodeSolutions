class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        sets={}
        sett={}
        for i in range(len(s)):
            sets[s[i]]=1+sets.get(s[i],0)
            sett[t[i]]=1+sett.get(t[i],0)
        for st in sets:
            if sets[st]!=sett.get(st,0):
                return False
        return True 