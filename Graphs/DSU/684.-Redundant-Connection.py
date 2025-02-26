class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent=[i for i in range(n+1)]
        rank=[0]*(n+1)

        def findRoot(i):
            if parent[i]!=i:
                parent[i]=findRoot(parent[i]) # path compression when this happens all nodes will point to the root parent[i] give the root , which gets updates every time and very easy for the next look up
            return parent[i]

            # while parent[i] != i:  # Traverse up until the root
            #     i = parent[i]
            # return i
        

        
        def merge(u,v):  # union by rank
            rootU=findRoot(u)
            rootV=findRoot(v)

            # if rootU != rootV:
            #     parent[rootU] = rootV  # Attach one tree to another  without rank This can create unbalanced trees, leading to inefficient findParent operations.ie large tree attached to small ones

            if rootU !=rootV:
                if rank[rootU]> rank[rootV]:
                    parent[rootV]=rootU
                elif rank[rootV]> rank[rootU]:
                    parent[rootU]=rootV
                else:
                    parent[rootU]=rootV
                    rank[rootV]+=1
        
        for u,v in edges:
            if findRoot(u)==findRoot(v):
                return[u,v]
            
            merge(u,v)
        
        return []
            
        