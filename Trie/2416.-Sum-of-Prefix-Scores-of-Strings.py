class TrieNode:
    def __init__(self):
        self.children={}
        self.count=0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root=TrieNode()
        # trie construction
        for word in words:
            node=root
            for char in word:
                if char not in node.children:
                    node.children[char]=TrieNode()
                node=node.children[char]
                node.count+=1

        res=[]
        for word in words:
            node=root
            sum1=0
            for char in word:
                node=node.children[char]
                sum1+=node.count
            res.append(sum1)
        return res

        
        
        # prefixSums={}

        # for word in words:
        #     wordLen=len(word)
        #     i=1
        #     while i<= wordLen:
        #         prefix=word[:i]
        #         if prefix in prefixSums:
        #             prefixSums[prefix]+=1
        #         else:
        #             prefixSums[prefix]=1
        #         i+=1
        # res=[]

        # for word in words:
        #     wordLen=len(word)
        #     i=1
        #     sum1=0
        #     while i<= wordLen:
        #         prefix=word[:i]
        #         if prefix in prefixSums:
        #             sum1+=prefixSums[prefix]
        #         i+=1
        #     res.append(sum1)
            
        # return res



        
                





        