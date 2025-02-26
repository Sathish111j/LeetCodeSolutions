class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1 and not trust:
            return 1

        indegree=[0]*(n+1)
        outdegree=[0]*(n+1)

        for u , v in trust:
            outdegree[u]+=1
            indegree[v]+=1
        
        for i in range(1,n+1):
            if indegree[i]==n-1 and outdegree[i]==0:
                return i

        return -1

        