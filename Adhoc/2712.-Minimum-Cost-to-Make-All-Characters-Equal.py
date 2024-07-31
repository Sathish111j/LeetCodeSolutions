class Solution:
    def minimumCost(self, s: str) -> int:
        res = 0
        length = len(s)
        for i in range(1 ,  length):
            if s[i - 1] != s[i]:
                res = res + min(i , length - i)
        return res