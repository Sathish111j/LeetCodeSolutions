class Solution:
    def strangePrinter(self, s: str) -> int:
        memo = {}

        def minPrints(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
                
            ans = 1 + minPrints(i + 1, j)
            for k in range(i + 1, j + 1):
                if s[k] == s[i]:
                    ans = min(ans, minPrints(i + 1, k - 1) + minPrints(k, j))
            memo[(i, j)] = ans
            return ans

        return minPrints(0, len(s) - 1)