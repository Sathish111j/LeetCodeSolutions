class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        p1=0
        p2=1
        totalWaitTime=0

        while p2 < len(colors):
            if colors[p1] ==colors[p2]:
                if neededTime[p1] < neededTime[p2]:
                    totalWaitTime+=neededTime[p1]
                    p1 =p2 
                else:
                    totalWaitTime+=neededTime[p2]
            else:
                p1 = p2 

            p2+=1 
        return totalWaitTime


                
            

            
