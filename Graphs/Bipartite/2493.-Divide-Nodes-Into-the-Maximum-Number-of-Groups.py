class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
# when not Bipartite connot is grouped as per condition
# calculate max depth to count max grups can be formed
# add all groups
        def isBipartite(node,c, component):
            color[node]=c
            component.append(node)

            for nei in adj[node]:
                if color[nei]==c:
                    return False
                if color[nei]==-1 and not isBipartite(nei,1-c,component):
                    return False
            
            return True

        def maxDepth(component):
            maxDepth=0

            for startNode in component:
                depth=[-1]*n
                queue=deque()
                queue.append(startNode)
                depth[startNode]=0

                while queue:
                    node=queue.popleft()
                    for nei in adj[node]:
                        if depth[nei]==-1:
                            depth[nei]=depth[node]+1
                            maxDepth=max(maxDepth,depth[nei])
                            queue.append(nei)
            return maxDepth +1 #depth to groups 
                        
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        
        color=[-1]*n
        components=[]

        for i in range(n):
            if color[i]==-1:
                component=[]
                if not isBipartite(i,0,component):
                    return -1
                components.append(component)

        groups=0
        
        for comp in components:
            groups+=maxDepth(comp)
        
        return groups