class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[-1] * n for _ in range(n)] for _ in range(n)]
        
        def dfs(r1, c1, r2):
            c2 = r1 + c1 - r2 
            if r1 == n or r2 == n or c1 == n or c2 == n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            
            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]
            
            if dp[r1][c1][r2] != -1:
                return dp[r1][c1][r2]

            result = grid[r1][c1]

            if r1 != r2:
                result += grid[r2][c2]

            result += max(dfs(r1, c1+1, r2),      # right, down
                          dfs(r1+1, c1, r2+1),    # down, down
                          dfs(r1, c1+1, r2+1),    # right, right
                          dfs(r1+1, c1, r2))      # down, right
            
            dp[r1][c1][r2] = result
            return result
        
        return max(0, dfs(0, 0, 0))
            
            
        
            
                
        