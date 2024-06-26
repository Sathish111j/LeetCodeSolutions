class Solution:
    def climbStairs(self, n: int) -> int:
        memo=[-1]*(n+1)
        
        def helper(n):
            if n ==0:
                return 1
            if n <0 :
                return 0
            if memo[n]!=-1:
                return memo[n]
            
            l=helper(n-1)
            r=helper(n-2)
            memo[n]=l+r

            return memo[n]
        return helper(n)
    
        

        