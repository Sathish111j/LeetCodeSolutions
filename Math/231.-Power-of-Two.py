class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n and not (n & n - 1)
    
# pow(2, n) & (pow(2, n) - 1) == 0
# for example, num = 4 = 0b100
# 4 - 1 = 3 = 0b11
# 4 & 3 = 0b100 & 0b11 = 0
