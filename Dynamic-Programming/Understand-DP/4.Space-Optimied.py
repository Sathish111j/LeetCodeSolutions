class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1] * n 
        for i in range(1, m):
            curr = [1] * n
            for j in range(1, n):
                curr[j] = prev[j] + curr[j-1]
            prev = curr[:]
        return prev[n-1]


# when ever in dp there is dp[i] = dp[i-1] + dp[i-2] we can use two variables to store the previous values
#this make it space optimized


# Approach	    Time Complexity	Space Complexity
# Recursive	       O(2^n)	      O(n)
# Memoization	   O(n)	          O(n)
# Tabulation	   O(n)	          O(n)
# Space-Optimized  O(n)	          O(1)