class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dp(i, j):
            if i == 0 and j == 0:  
                return 1
            if i < 0 or j < 0:  
                return 0
            
            up = dp(i-1, j)    
            left = dp(i, j-1) 
            return up + left
        
        return dp(m-1, n-1)
