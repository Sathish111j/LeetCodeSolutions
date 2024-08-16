class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        maxDistance = 0
        initialMin, initialMax = arrays[0][0], arrays[0][-1]
        for i in range(1, len(arrays)):
            currMin = arrays[i][0]
            currMax = arrays[i][-1]
            maxDistance = max(maxDistance, abs(currMax - initialMin), abs(initialMax - currMin))
            initialMin = min(initialMin, currMin)
            initialMax = max(initialMax, currMax)

        return maxDistance