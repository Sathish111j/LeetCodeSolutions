def solve(height):
    n = len(height)
    prev = 0
    prev2 = 0
    for i in range(1, n):
        jumpOne = prev + abs(height[i] - height[i - 1])
        jumpTwo = float('inf')
        if i > 1:
            jumpTwo = prev2 + abs(height[i] - height[i - 2])
        cur_i = min(jumpOne, jumpTwo)
        prev2 = prev
        prev = cur_i
    return prev

# when ever in dp there is dp[i] = dp[i-1] + dp[i-2] we can use two variables to store the previous values
#this make it space optimized