class Solution:
    def punishmentNumber(self, n: int) -> int:

        def check(x,target):
            s=str(x)
            n=len(s)

            def dfs(i,currSum):
                if i==n:
                    return currSum==target
                num=0

                for j in range(i,n):
                    num=num*10+int(s[j])
                    if dfs(j+1,currSum+num):
                        return True
                return False
            return dfs(0,0)

        return sum(i*i for i in range(1,n+1 )if check(i*i,i))