class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
         # to store the graph connections
        graph = {}
        
        # build the graph
        for x, y in stones:
            if x not in graph:
                graph[x] = []
            if ~y not in graph:
                graph[~y] = []
            graph[x].append(~y)
            graph[~y].append(x)
        
        # to track visited nodes
        visited = set()
        
        def dfs(node):
            stack = [node]
            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    for neighbor in graph[current]:
                        if neighbor not in visited:
                            stack.append(neighbor)
        
        # Counting connected components
        components = 0
        for x, y in stones:
            if x not in visited:
                dfs(x)
                components += 1
        
        # the number of stones that can be removed is total stones minus the number of connected components
        return len(stones) - components