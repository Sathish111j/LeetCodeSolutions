class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1=0
        p2=0
        merged=[]
        while len(merged)!=len(word1)+len(word2) and p1<len(word1 ) and p2<len(word2):
            merged.append(word1[p1])
            merged.append(word2[p2])
            p1+=1
            p2+=1
        merged+=word1[p1:]
        merged+=word2[p2:]
        return "".join(merged)

