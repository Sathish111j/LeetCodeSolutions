class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # m, n = len(points), len(points[0])
        # memo = {}

        # def dfs(row, col):
        #     if (row, col) in memo:
        #         return memo[(row, col)]
        #     if row == m:
        #         return 0
        #     maxScore = 0
        #     for nextCol in range(n):
        #         cost = abs(col - nextCol)
        #         maxScore = max(maxScore, points[row][col] + dfs(row + 1, nextCol) - cost)
        #     memo[(row, col)] = maxScore
        #     return maxScore
        
        # maxResult = 0
        # for startCol in range(n):
        #     maxResult = max(maxResult, dfs(0, startCol))
        # return maxResult
            
        rows, cols = len(points), len(points[0])
        dp = [[-1] * cols for _ in range(rows)]
        left = [float('-inf')] * cols
        right = [float('-inf')] * cols

        def calculateMaxPoints(i, j):
            if i == 0:
                return points[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            if j == 0:
                computeMaxFromLeftAndRight(i)
            dp[i][j] = max(left[j], right[j]) + points[i][j]
            return dp[i][j]

        def computeMaxFromLeftAndRight(i):
            left[0] = calculateMaxPoints(i-1, 0)
            for j in range(1, cols):
                left[j] = max(left[j-1] - 1, calculateMaxPoints(i-1, j))

            right[cols-1] = calculateMaxPoints(i-1, cols-1)
            for j in range(cols-2, -1, -1):
                right[j] = max(right[j+1] - 1, calculateMaxPoints(i-1, j))

        maxResult = 0
        for j in range(cols):
            maxResult = max(maxResult, calculateMaxPoints(rows-1, j))
        return maxResult