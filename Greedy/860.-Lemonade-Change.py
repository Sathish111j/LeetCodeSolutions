class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # bills.sort()
        _5count=0
        _10count=0


        for bill in bills:
            if bill==5:
                _5count+=1
            elif bill==10:
                if _5count == 0:
                    return False
                _5count -= 1
                _10count += 1
            else:
                if _10count > 0 and _5count >0:
                    _10count -= 1
                    _5count -= 1
                elif _5count >2:
                    _5count -= 3
                else:
                    return False
                    
        return True


            