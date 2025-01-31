class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        n=len(grid)
        islandSizes={}
        islandID=2

        def maxSizeDfs(r,c,id):
            if r<0 or r>=n or c<0 or c>=n or grid[r][c]!=1:
                return 0
            size=1
            grid[r][c]=id

            for x,y in directions:
                size+=maxSizeDfs(r+x,c+y,id)
            return size
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    islandSizes[islandID]=maxSizeDfs(i,j,islandID)
                    islandID+=1

        def isConnected(i,j):
            connectedIslandsID=set()
            for x,y in directions:
                nx,ny=i+x,j+y
                if 0<=nx<n and 0<=ny<n and grid[nx][ny]>1:
                    connectedIslandsID.add(grid[nx][ny])
            
            totalSize=1 #1 because 0-> 1 turned need to inlcude that
            for islandID in connectedIslandsID:
                totalSize+=islandSizes[islandID]
            
            return totalSize

        
        maxSize=max(islandSizes.values(),default=0)
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    maxSize=max(maxSize,isConnected(i,j))
        return maxSize
        







    
