class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        p1=len(g)-1
        p2=len(s)-1
        
        result=0

        while p1!=-1 and p2!=-1:
            if g[p1]<=s[p2]:
                p1-=1
                p2-=1
                result+=1
                
            else:
                p1-=1

        return result



