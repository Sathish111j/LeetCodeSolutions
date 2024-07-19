class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        luckNumbers=[]
        n=len(matrix)
        m=len(matrix[0])

        for i in range(len(matrix)):
            index=-1
            num=float("inf")

            # row min
            for j in range(m):
                if matrix[i][j]<num:
                    num=matrix[i][j]
                    index=j
            

            # check if its max in col
            isLucky=True
            for k in range(n):
                if matrix[k][index]>num:
                    isLucky=False
                    break
            
            if isLucky:
                luckNumbers.append(num)
            

        return luckNumbers

                
        
        



        