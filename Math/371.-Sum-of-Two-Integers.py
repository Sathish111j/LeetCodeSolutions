class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask=0xffffffff 
        # in python the number are not represent in 32 its like other languages it has more bits and to non negative ie 2's complement , we need only 8 bit here hence use mask ie x&1=x similarly 0xffffffff we take only the last 8 bits here
        while b & mask!=0:
            carry=(a&b)<<1
            a=a^b
            b=carry
        
        if b>0:
            return a&mask
        else:
            return a