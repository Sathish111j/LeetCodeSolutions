class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        top,bottom,left,right=0,n-1,0,n-1
        res=[[0]*n for _ in range(n)]
        count=1


        while count<=n*n:

            for col in range(left,right+1):
                res[top][col]=count
                count+=1
            top+=1
           

            for row in range(top,bottom+1):
                res[row][right]=count
                count+=1
            right-=1
            

            for col in range(right,left-1,-1):
                res[bottom][col]=count
                count+=1
            bottom-=1

            for row in range(bottom,top-1,-1):
                res[row][left]=count
                count+=1
            left+=1

        
        return res


