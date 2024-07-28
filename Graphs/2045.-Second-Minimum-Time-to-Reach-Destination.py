class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # Create the graph using a defaultdict of lists
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # priority queue for Dijkstra's algorithm
        q = []
        heapq.heappush(q, (0, 1))  # (time, node)
        
        uniqueVisit = [0] * (n + 1)  # to track the number of unique visits
        dis = [-1] * (n + 1)  # to store the minimum time to reach each node
        
        while q:
            t, node = heapq.heappop(q)  # get the node with the smallest time
            
            if dis[node] == t or uniqueVisit[node] >= 2:
                continue  # skip if already visited or relaxed twice
            
            uniqueVisit[node] += 1
            dis[node] = t
            
            if node == n and uniqueVisit[node] == 2:
                return dis[node]
            
            # calculate the leaving time (waiting for the green light)
            if (t // change) % 2 != 0:
                t = (t // change + 1) * change
            
            for nei in g[node]:
                heapq.heappush(q, (t + time, nei))
        
        return -1