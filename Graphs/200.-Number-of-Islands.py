class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        m=len(grid)
        n=len(grid[0])

        visited=[[0]*n for _ in range(m)]

        def bfs(i,j):
            queue=deque([(i,j)])
            visited[i][j]=1
            direction=[(0,1),(1,0),(0,-1),(-1,0)]

            while queue:
                x,y=queue.popleft()
                for dx, dy in direction:
                    nx,ny=x+dx , y+dy

                    if 0<=nx<m and 0<=ny<n and not visited[nx][ny] and grid[nx][ny]=='1':
                        queue.append((nx,ny))
                        visited[nx][ny]=1

        count=0

        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and not visited[i][j]:
                    count+=1
                    bfs(i,j)
        return count



