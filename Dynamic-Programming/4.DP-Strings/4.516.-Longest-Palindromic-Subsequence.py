class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        # this is same as longest common subsequence 
        text1=s
        text2=s[::-1]

        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        # TO SHOW THE BASE CASE NO NEED FOR THIS AS ALREADY ALL RARE INITILIZED WITH 0
        for i in range(len(text1) + 1):
            dp[i][0] = 0
        for j in range(len(text2) + 1):
            dp[0][j] = 0

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[len(text1)][len(text2)]