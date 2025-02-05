class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        graph=defaultdict(list)
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        colors={}

        def bfs(start):
            queue=deque([start])
            colors[start]=0

            while queue:
                node=queue.popleft()

                for nei in graph[node]:
                    if nei in colors:
                        if colors[nei]==colors[node]:
                            return False
                    else:
                        colors[nei]=1-colors[node]
                        queue.append(nei)
            return True


        for i in range(1,n+1):
            if i not in colors:
                if not bfs(i):
                    return False
        return True


        # # Traverse all nodes (to handle disconnected components)
        # for i in range(1, n + 1):
        #     if i not in colors:  # If the node is unvisited, start BFS
        #         components += 1
        #         if not bfs(i):
        #             return False
        #         if components > k:  # More groups than allowed
        #             return False





