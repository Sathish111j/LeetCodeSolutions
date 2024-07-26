class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distance=[[float("inf")]* n for _ in range(n)]

        #distance to itself

        for i in range(n):
            distance[i][i]=0

        for u , v,w in edges:
            distance[u][v]=w
            distance[v][u]=w
        
        #floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if distance[i][j]>distance[i][k] + distance[k][j]:
                        distance[i][j] = distance[i][k] + distance[k][j]
        
        #city with the smallest number of reachable cities
        minReachableCities = float('inf')
        bestCity = -1
        
        for i in range(n):
            reachableCities = 0
            for j in range(n):
                if distance[i][j] <= distanceThreshold:
                    reachableCities += 1
            
            if reachableCities <= minReachableCities:
                minReachableCities = reachableCities
                bestCity = i
        
        return bestCity