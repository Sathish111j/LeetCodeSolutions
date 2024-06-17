class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split(" ")

        result=[]
        for word in words:
            result.append(self.reverse(word))
        
        return " ".join(result)



    def reverse(self,word):
        word_list = list(word)
        l=0
        r=len(word_list)-1

        while l<r:
            word_list[l],word_list[r]=word_list[r],word_list[l]
            l+=1
            r-=1

        
        return "".join(word_list)
         
    
        