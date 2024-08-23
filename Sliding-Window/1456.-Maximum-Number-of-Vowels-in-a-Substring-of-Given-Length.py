class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        l=0
        noOfVowels=0
        maxVowels=0

        vowels={'a','e','i','o','u'}

        for r in range(len(s)):
            if r<k:
                if s[r] in vowels :
                    noOfVowels+=1
            else:
                if s[r] in vowels :
                    noOfVowels+=1
                if s[l] in vowels:
                    noOfVowels-=1
                l+=1
                
            maxVowels=max(maxVowels,noOfVowels)
            if maxVowels==k:
                    return maxVowels
        return maxVowels
                


                
