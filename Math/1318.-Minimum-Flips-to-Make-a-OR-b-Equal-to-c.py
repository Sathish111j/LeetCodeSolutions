class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips=0

        while a>0 or b>0 or c>0 :
            aBit=a&1
            bBit=b&1
            cBit=c&1

            if cBit==0:
                flips+= aBit+bBit # when c is zero and a is 1 b is 1 then 2 flips else 1 flip or 0 flips 
            else:# when cbit==1
                if aBit==0 and bBit==0: 
                    flips+=1 # any of a or b flip is enough
            
            a=a>>1
            b=b>>1
            c=c>>1
        
        return flips

