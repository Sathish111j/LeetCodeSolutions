class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score=[]
        for operation in operations:
            if operation=="C":
                score.pop()
            elif operation=="+":
                score.append(score[-1]+score[-2])
            elif operation=="D":
                score.append(score[-1]*2)
            else:
                score.append(int(operation))
        return sum(score)

            