class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # we can generate all subsequence of biothj and store in hashmap and find the common which is exponential 2^n
        #can be genrated with recurrsion or power set

        # def generate_subsequences(s):
        #     subsequences = []

        #     def generate(index, current):
        #         if index == len(s):
        #             subsequences.append(current)
        #             return
        #         # Include the current character
        #         generate(index + 1, current + s[index])
        #         # Exclude the current character
        #         generate(index + 1, current)

        #     generate(0, "")
        #     return subsequences

        
        # def generate_subsequences(s):
        #     n = len(s)
        #     power_set_size = 1 << n  # 2^n, using bitwise shift for efficiency
        #     subsequences = []

        #     for i in range(power_set_size):
        #         subsequence = ""
        #         for j in range(n):
        #             if i & (1 << j):  # Check if jth bit in i is set
        #                 subsequence += s[j]
        #         subsequences.append(subsequence)
            
        #     return subsequences


#SHIFTING OD INDEX HAS BEEN DONE -1 IS TREADED AS 0 AND SO ON , THIS IS DONE FOR TABULATION AS WE CANT STORE -1 PLACE AS SHIFTING HAS BEEB DONE 

        # def lcsRecursive(text1, text2, i, j):
        #     if i == 0 or j == 0:
        #         return 0
        #     if text1[i - 1] == text2[j - 1]:
        #         return 1 + lcsRecursive(text1, text2, i - 1, j - 1)
        #     else:
        #         return max(lcsRecursive(text1, text2, i - 1, j), lcsRecursive(text1, text2, i, j - 1))

        # def longestCommonSubsequence(text1, text2):
        #     return lcsRecursive(text1, text2, len(text1), len(text2))

        

        # def lcsMemoization(text1, text2, i, j, dp):
        #     if i == 0 or j == 0:
        #         return 0
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     if text1[i - 1] == text2[j - 1]:
        #         dp[i][j] = 1 + lcsMemoization(text1, text2, i - 1, j - 1, dp)
        #     else:
        #         dp[i][j] = max(lcsMemoization(text1, text2, i - 1, j, dp), lcsMemoization(text1, text2, i, j - 1, dp))
        #     return dp[i][j]

        # def longestCommonSubsequence(text1, text2):
        #     dp = [[-1 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        #     return lcsMemoization(text1, text2, len(text1), len(text2), dp)
        

        # def longestCommonSubsequenceTabulation(text1, text2):
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

