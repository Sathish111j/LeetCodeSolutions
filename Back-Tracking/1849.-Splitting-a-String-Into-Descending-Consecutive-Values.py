class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(index,previous):
            if index==len(s):
                return True
            for j in range(index,len(s)):
                val=int(s[index:j+1])
                if val+1==previous:
                    if dfs(j+1,val):
                        return True
            return False

        for i in range(len(s)-1): # check from 1 digit 2 digit and soo on
            val=int(s[:i+1])
            if dfs(i+1,val):
                return True
        
        return False
