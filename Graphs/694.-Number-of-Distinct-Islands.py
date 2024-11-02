class Solution:
    def numDistinctIslands(self, grid):
        def dfs(x, y, base_x, base_y, shape):
            shape.add((x - base_x, y - base_y))
            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not visited[nx][ny] and grid[nx][ny] == 1:
                    dfs(nx, ny, base_x, base_y, shape)

        if not grid or not grid[0]:
            return 0

        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        unique_islands = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j]:
                    shape = set()
                    dfs(i, j, i, j, shape)  
                    unique_islands.add(tuple(shape))  # Convert shape to tuple to store in set

        return len(unique_islands)

solution = Solution()

solution.numDistinctIslands([
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
])
# Output: 3

solution.numDistinctIslands([
    [1, 1, 0, 1, 1],    
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1]
])  
# Output: 2

#time complexity: O(m*n)
#space complexity: O(m*n)