class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        maxSideLenght=sum(matchsticks)//4

        sides=[0]*4
        if sum(matchsticks)/4!=sum(matchsticks)//4 :# whne comes in floating point
            return False
        matchsticks.sort(reverse=True) # for early stoping
        
        def backtracking(i):
            if i==len(matchsticks):
                return True
            
            for j in range(4):
                if sides[j]+matchsticks[i]<=maxSideLenght:
                    sides[j]+=matchsticks[i]
                    if backtracking(i+1):# if atleast one case is true return Truw
                        return True
                    sides[j]-=matchsticks[i]
            return False

        return backtracking(0)
