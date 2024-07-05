def solve(ind, height):
    if ind == 0:
        return 0
    jumpOne = solve(ind-1, height) + abs(height[ind] - height[ind-1])
    jumpTwo = float('inf')
    if ind > 1:
        jumpTwo = solve(ind-2, height) + abs(height[ind] - height[ind-2])
    return min(jumpOne, jumpTwo)