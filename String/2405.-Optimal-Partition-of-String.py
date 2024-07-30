class Solution:
    def partitionString(self, s: str) -> int:
        result=0
        substring=set()
        for char in s:
            if char in substring:
                result+=1
                substring.clear()
            substring.add(char)

        if char in substring:
            result+=1
            
        return result