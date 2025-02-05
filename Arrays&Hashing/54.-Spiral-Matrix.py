class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res=[]
        n=len(matrix[0])
        m=len(matrix)

        top,bottom=0,m-1
        left,right=0,n-1
    

        while len(res) < m * n:

            for col in range(left,right+1):
                res.append(matrix[top][col])
            top+=1
            if len(res) >= m * n: break

            for row in range(top,bottom+1):
                res.append(matrix[row][right])
            right-=1
            if len(res) >= m * n: break

            for col in range(right,left-1,-1):
                res.append(matrix[bottom][col])
            bottom-=1
            if len(res) >= m * n: break
            
            for row in range(bottom,top-1,-1):
                res.append(matrix[row][left])
            left+=1
        
        return res