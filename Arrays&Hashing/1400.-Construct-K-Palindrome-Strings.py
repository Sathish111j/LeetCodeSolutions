class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        if len(s)<k:
            return False
        
        fre=Counter(s)

        c=0
        for key,value in fre.items():
            if value%2==1:
                c+=1
        if c>k:
            return False

        return True