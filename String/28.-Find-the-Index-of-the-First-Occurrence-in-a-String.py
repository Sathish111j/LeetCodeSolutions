class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # return haystack.find(needle)

        m, n = len(haystack), len(needle)
        if n == 0: 
            return 0
        if m < n:  
            return -1
        for i in range(m - n + 1):
            if haystack[i:i + n] == needle:
                return i
        return -1