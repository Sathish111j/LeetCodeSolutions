class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph={i:[] for i in range(n)}

        for child ,parent in edges:
            graph[child].append(parent)
            graph[parent].append(child)

        def dfs(current ,par):
            time=0
            for child in graph[current]:
                if child==par:
                    continue
                child_time = dfs(child,current)
                if child_time or hasApple[child]:
                    time+=2+child_time
            return time
        return dfs(0,-1)