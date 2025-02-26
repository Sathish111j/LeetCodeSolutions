
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(list)

        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        queue=deque([source])
        visited=set()

        while queue:
            node=queue.popleft()
            if node==destination:
                return True
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    queue.append(nei)

        
        return False
#bfs time complexity is O(n) and space complexity is O(n)
            
# Union Find time complexity is O(n) and space complexity is O(n) but this is faster than bfs
#because in bfs we are traversing all the nodes but in union find we are just checking if the source and destination are connected or not
def validPath(self, n: int, edges: List[List[int]], source: int, destination: int)->bool:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        p = list(range(n))
        for u, v in edges:
            p[find(u)] = find(v)
        return find(source) == find(destination)