class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        indexOf={}
        
        sortedScore=sorted(score, reverse=True)
        for i in range(len(score)):
            indexOf[sortedScore[i]]=i

 

        for athelete in range(len(score)):
            indexOfathelete=indexOf[score[athelete]]
            if indexOfathelete ==0:
                score[athelete]="Gold Medal"
            elif indexOfathelete==1:
                score[athelete]="Silver Medal"
            elif indexOfathelete==2:
                score[athelete]="Bronze Medal"
            else:
                score[athelete]=str(indexOfathelete+1)

        return score