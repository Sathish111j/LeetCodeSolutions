class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # result=[]
        # for i in range(len(matrix)):
        #     temp=[]
        #     for j in range(len(matrix)-1,-1,-1):
        #         temp.append(matrix[j][i])
        #     result.append(temp)

        # for i in range(len(matrix)):
        #     for j in range(len(matrix)):
        #         matrix[i][j] = result[i][j]

        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            matrix[i].reverse()

       