class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(sr,sc,initialcolor): # bfs can be used too
            image[sr][sc]=color
            for dr,dc in newRowCols:
                nr ,nc=sr+dr,sc+dc

                if  0 <= nr < n and 0 <= nc < m  and image[nr][nc]==initialcolor:
                    dfs(nr,nc,initialcolor)
        

        n=len(image)
        m=len(image[0])
        newRowCols=[(1,0),(0,1),(-1,0),(0,-1)]
        initialColor=image[sr][sc]

        if initialColor == color:
            return image
        dfs(sr,sc,initialColor)
        return image

