class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # memo = {}
        # def dfs(i):
        #     if i in memo:
        #         return memo[i]
        #     if i == len(books):
        #         return 0
        #     minHeight = float('inf')
        #     currentWidth, currentHeight = 0, 0
        #     for j in range(i, len(books)):
        #         currentWidth += books[j][0]
        #         if currentWidth > shelfWidth:
        #             break
        #         currentHeight = max(currentHeight, books[j][1])
        #         minHeight = min(minHeight, currentHeight + dfs(j + 1))
        #     memo[i] = minHeight
        #     return minHeight
        
        # return dfs(0)


        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            width, height = 0, 0
            for j in range(i - 1, -1, -1):
                width += books[j][0]
                if width > shelfWidth:
                    break
                height = max(height, books[j][1])
                dp[i] = min(dp[i], dp[j] + height)
        
        return dp[n]