# A bipartite graph is which all the node can be colored using
#two colors such that no two adjacent nodes have the same color.

# All linear graphs are bipartite graphs.

# A graph with cylces is bipartite if the length of all the cycles is even.

# A graph with odd length cycles is not bipartite.

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        def bfs(start,graph,color):
            queue = deque([(start, 0)])  # Start with color 0
            color[start] = 0  # Initial color
            
            while queue:
                node, col = queue.popleft()
                
                for neighbor in graph[node]:
                    if color[neighbor] == -1:  # If the neighbor is uncolored
                        color[neighbor] = 1 - col  # Assign the opposite color
                        queue.append((neighbor, color[neighbor]))
                    elif color[neighbor] == col:  # If the neighbor has the same color
                        return False  
            
            return True
        
        n = len(graph)
        color = [-1] * n  
        
        for i in range(n):
            if color[i] == -1:  # If the node is unvisited
                if not bfs(i, graph, color):
                    return False
        
        return True
        
        
        