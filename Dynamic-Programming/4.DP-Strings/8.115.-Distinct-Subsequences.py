def numDistinct(s: str, t: str) -> int:
    n, m = len(s), len(t)
    memo = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]

    def dp(i, j):
        if j == 0:  # If t is empty, there's always one way to match it
            return 1
        if i == 0:  # If s is empty but t is not, there's no way to match
            return 0
        if memo[i][j] != -1:
            return memo[i][j]
        
        if s[i - 1] == t[j - 1]:
            memo[i][j] = dp(i - 1, j - 1) + dp(i - 1, j)  # Take or skip
        else:
            memo[i][j] = dp(i - 1, j)  # Only skip
        
        return memo[i][j]
    
    return dp(n, m)
# Time complexity: O(n * m)
# Space complexity: O(n * m) + O(n + m) 



def numDistinct(s: str, t: str) -> int:
    n, m = len(s), len(t)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # Base case: dp[i][0] = 1 for all i
    for i in range(n + 1):
        dp[i][0] = 1

    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]  # Take or skip
            else:
                dp[i][j] = dp[i - 1][j]  # Skip
        
    return dp[n][m]
# Time complexity: O(n * m)
#space complexity: O(n * m)


def numDistinct(s: str, t: str) -> int:
    n, m = len(s), len(t)
    prev = [0] * (m + 1)
    curr = [0] * (m + 1)

    # Base case: prev[0] = 1 (an empty t can always be matched)
    prev[0] = 1

    # Fill the dp array row by row
    for i in range(1, n + 1):
        curr[0] = 1  # Every dp[i][0] is 1
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                curr[j] = prev[j - 1] + prev[j]  # Take or skip
            else:
                curr[j] = prev[j]  # Skip
        
        # Move the current row to the previous row for the next iteration
        prev = curr[:]

    return prev[m]
# Time complexity: O(n * m)
# Space complexity: O(m)


def numDistinct(s: str, t: str) -> int:
    n, m = len(s), len(t)
    dp = [0] * (m + 1)

    # Base case: dp[0] = 1
    dp[0] = 1

    # Fill the dp array
    for i in range(1, n + 1):
        # Traverse backwards to prevent overwriting
        for j in range(m, 0, -1):
            if s[i - 1] == t[j - 1]:
                dp[j] = dp[j - 1] + dp[j] # Update current based on previous

    return dp[m]
# Time complexity: O(n * m)
# Space complexity: O(m)