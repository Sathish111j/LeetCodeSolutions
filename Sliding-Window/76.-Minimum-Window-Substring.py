class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l=0
        n,m=len(s),len(t)
        cnt=0
        minlen=float("inf")
        startind=-1
        mp=Counter(t)

        for r in range(n):
            if s[r] in  mp and mp[s[r]]>0:
                cnt+=1
            if s[r] in mp:
                mp[s[r]]-=1
            
            while cnt ==m:
                if r-l+1 < minlen:
                    minlen=r-l+1
                    startind=l
                
                if s[l] in mp:
                    mp[s[l]]+=1
                    if mp[s[l]]>0:
                        cnt-=1
                l+=1
        
        if startind ==-1:
            return ""
        else:
            return s[startind:startind+minlen]