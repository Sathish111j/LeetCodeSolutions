class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        dir=[(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(i,j):
            
            visited[i][j]=1
            for r,c in dir:
                nr,nc=i+r,j+c

                if 0<=nr<n and 0<=nc<m and not visited[nr][nc] and grid[nr][nc]:
                    dfs(nr,nc)
                    


        n,m=len(grid),len(grid[0])

        visited=[[0]*m for _ in range(n)]

        for j in range(m):
            if grid[0][j]==1:
                dfs(0,j)
            if grid[n-1][j]==1:
                dfs(n-1,j)

        for i in range(n):
            if grid[i][0]==1:
                dfs(i,0)
            if grid[i][m-1]==1:
                dfs(i,m-1)
        count=0
        for i in range(n):
            for j in range(m):
                if not visited[i][j]  and grid[i][j]:
                    count+=1
        return count