import math
class ProductOfNumbers:

    def __init__(self):
        self.pre_mul = []
        self.product = 1
        
    def add(self, num: int) -> None:
        if num is not 0:
            self.product *= num
            self.pre_mul.append(self.product)
        else:
            self.product = 1
            self.pre_mul = []

    def getProduct(self, k: int) -> int:
        if k == len(self.pre_mul):
            return self.pre_mul[-1]
        elif k > len(self.pre_mul):
            return 0
        else:
            return int(self.pre_mul[-1]/self.pre_mul[-1-k])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)