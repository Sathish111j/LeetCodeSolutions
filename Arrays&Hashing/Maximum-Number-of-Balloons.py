class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashset=defaultdict(int)
        
        for c in text:
            hashset[c]+=1

        return min([hashset['b'],hashset['a'],hashset['l']//2,hashset['o']//2,hashset['n']])