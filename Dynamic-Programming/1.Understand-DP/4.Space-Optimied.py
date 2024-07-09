class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1] * n 
        for i in range(m):
            curr = [1] * n 
            for j in range(n):
                if i == 0 and j == 0:
                    curr = 1
                else:
                    up,left=0,0
                    if i>0:
                        up = prev[j] 
                    if j>0:
                        left =curr[j-1]
                    curr[j]=up+left
            prev = curr[:]
        return prev[n-1]

# when ever in dp there is dp[i] = dp[i-1] + dp[i-2] we can use two variables to store the previous values
#this make it space optimized
#Just replace all [i-1] → with prev and [i] → with curr 

# Approach	    Time Complexity	Space Complexity
# Recursive	       O(2^n)	      O(n)
# Memoization	   O(n)	          O(n) + recursion stack
# Tabulation	   O(n)	          O(n)
# Space-Optimized  O(n)	          O(1)