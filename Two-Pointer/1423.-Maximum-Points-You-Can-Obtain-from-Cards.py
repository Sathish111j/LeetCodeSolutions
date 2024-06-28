class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maxsum=sum(cardPoints[:k])
        l=k
        r=0
        currentsum=maxsum


        for i in range(k):
            l-=1
            r-=1

            currentsum+= -cardPoints[l]+ cardPoints[r]

            if currentsum > maxsum:
                maxsum=currentsum
        
        return maxsum
            

        


            

