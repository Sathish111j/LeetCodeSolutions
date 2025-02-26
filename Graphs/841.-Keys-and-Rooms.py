class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph=defaultdict(list)

        n=0
        for keys in rooms:
            graph[n]=keys
            n+=1
        
        visited=set()
        queue=deque([0])

        while queue:
            node=queue.popleft()
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    queue.append(nei)
        
        return len(visited) == len(rooms)



        

