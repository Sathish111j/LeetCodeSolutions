class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
         # this is same as longest common subsequence 
        text1=word1
        text2=word2

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
        
        lenOfLong=dp[len(text1)][len(text2)] #lenghtOfLongestCommonSubSequence

        noOfDeletions=len(word1)-lenOfLong
        noOfInsertions=len(word2)-lenOfLong

        return  noOfDeletions + noOfInsertions

