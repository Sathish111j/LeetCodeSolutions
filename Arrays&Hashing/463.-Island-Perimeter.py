class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        s = set()
        a, b = len(grid), len(grid[0])

        def dfs(i, j):
            if i >= a or j >= b or i < 0 or j < 0 or grid[i][j] == 0:
                return 1

            if (i, j) in s:
                return 0
            
            s.add((i, j))
            pm = dfs(i, j + 1)
            pm += dfs(i + 1, j)
            pm += dfs(i - 1, j)
            pm += dfs(i, j - 1)
            return pm

        for i in range(a):
            for j in range(b):
                if grid[i][j]:
                    return dfs(i, j)