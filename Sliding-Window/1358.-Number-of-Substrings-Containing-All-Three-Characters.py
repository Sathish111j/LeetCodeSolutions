class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lastseen = {'a': -1, 'b': -1, 'c': -1}
        count=0

        for i in range(len(s)):
            lastseen[s[i]]=i
            if  lastseen['a']!=-1 and lastseen['b']!=-1 and lastseen['c']!=-1:
                count+=min(lastseen.values())+1
        return count

        