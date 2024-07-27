class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        CHAR_COUNT = 26  
        INF = float('inf') 
        
     
        graph = [[INF] * CHAR_COUNT for _ in range(CHAR_COUNT)]
        
        # cost to convert a character to itself is 0
        for i in range(CHAR_COUNT):
            graph[i][i] = 0
        
        #  graph with the given conversion costs
        for i in range(len(cost)):
            fromChar = ord(original[i]) - ord('a')
            toChar = ord(changed[i]) - ord('a')
            graph[fromChar][toChar] = min(graph[fromChar][toChar], cost[i])
        
        # conversion paths using the Floyd-Warshall algorithm
        for k in range(CHAR_COUNT):
            for i in range(CHAR_COUNT):
                if graph[i][k] < INF:
                    for j in range(CHAR_COUNT):
                        if graph[k][j] < INF:
                            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        
        #  total conversion cost from source to target
        totalCost = 0
        for i in range(len(source)):
            sourceChar = ord(source[i]) - ord('a')
            targetChar = ord(target[i]) - ord('a')
            if sourceChar != targetChar:
                if graph[sourceChar][targetChar] == INF:
                    return -1  
                totalCost += graph[sourceChar][targetChar]
        
        return totalCost