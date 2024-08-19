class Solution:
    def minSteps(self, n: int) -> int:
        memo = {}
        
        def backtrack(string, clipboard, count):
            if len(string) == n:
                return count
            if len(string) > n:
                return float("inf")
            key = (string, clipboard)
            if key in memo: 
                return memo[key]
            
            copy = backtrack(string, string, count + 1) if string != clipboard else float("inf")
            paste = backtrack(string + clipboard, clipboard, count + 1) if clipboard else float("inf")
            
            memo[key] = min(copy, paste)
            return memo[key]
        
        return backtrack("A", "", 0)