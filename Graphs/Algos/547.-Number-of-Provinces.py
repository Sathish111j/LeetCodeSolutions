class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj=defaultdict(list)
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]==1 and i!=j:
                    adj[i].append(j)
                    adj[j].append(i)
        visited=[0]*len(isConnected)

        count=0

        def dfs(node):
            visited[node]=1
            for n in adj[node]:
                if not visited[n]:
                    dfs(n)


        for i in range(len(isConnected)):
            if not visited[i]:
                count+=1
                dfs(i)
        
        return count

