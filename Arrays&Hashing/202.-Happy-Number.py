class Solution:
    # def isHappy(self, n: int) -> bool:   #using hashmaps
    #     dict={}
    #     ans=n
    #     while ans != 1:
    #         ans=self.findsqaures(ans)
    #         if ans in dict:
    #             return False
    #         else:
    #             dict[ans]=ans
    #     return True

    def isHappy(self, n: int) -> bool:  #using fast annd slow pointer
        slow=n
        fast=n

        while True:
            slow=self.findsqaures(slow)
            fast=self.findsqaures(self.findsqaures(fast))
            if slow==fast:
                break
        if slow ==1:
            return True
        return False

    def findsqaures(self,num):
        sum_of_squares = 0
        while num > 0:
            digit = num % 10
            sum_of_squares += digit ** 2
            num = num // 10
        return sum_of_squares