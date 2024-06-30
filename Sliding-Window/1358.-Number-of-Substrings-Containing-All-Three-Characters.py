class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lastseen = {'a': -1, 'b': -1, 'c': -1}
        count=0

        for i in range(len(s)):
            lastseen[s[i]]=i
            if  lastseen['a']!=-1 and lastseen['b']!=-1 and lastseen['c']!=-1:
                count+=min(lastseen.values())+1
        return count

        # can be done with list too
        #  last_seen = [-1, -1, -1]  # Index 0 for 'a', 1 for 'b', 2 for 'c'
        #  last_seen[ord(char) - ord('a')] = i