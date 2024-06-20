class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if  not digits:
            return []
        result=[]

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i,current):
            if i==len(digits):
                result.append(current)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i+1,current+c)
        backtrack(0,"")
        return result

