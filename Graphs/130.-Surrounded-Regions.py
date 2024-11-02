class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dir=[(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(i,j):
            
            visited[i][j]=1
            for r,c in dir:
                nr,nc=i+r,j+c

                if 0<=nr<n and 0<=nc<m and not visited[nr][nc] and board[nr][nc]=='O':
                    dfs(nr,nc)
                    


        n,m=len(board),len(board[0])

        visited=[[0]*m for _ in range(n)]

        for j in range(m):
            if board[0][j]=='O':
                dfs(0,j)
            if board[n-1][j]=='O':
                dfs(n-1,j)

        for i in range(n):
            if board[i][0]=='O':
                dfs(i,0)
            if board[i][m-1]=='O':
                dfs(i,m-1)
        
        for i in range(n):
            for j in range(m):
                if not visited[i][j]  and board[i][j]=="O":
                    board[i][j]='X'
        



        


