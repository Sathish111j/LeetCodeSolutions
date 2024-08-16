class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        maxDistance = 0
        prevMin, prevMax = arrays[0][0], arrays[0][-1]
        for i in range(1, len(arrays)):
            currMin = arrays[i][0]
            currMax = arrays[i][-1]
            maxDistance = max(maxDistance, abs(currMax - prevMin), abs(prevMax - currMin))
            prevMin = min(prevMin, currMin)
            prevMax = max(prevMax, currMax)

        return maxDistance