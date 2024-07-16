class Solution:
    def queryString(self, s: str, n: int) -> bool:
        def DecimalToBinary(num):
            binary_str = ""
            while num > 0:
                binary_str = str(num % 2) + binary_str
                num //= 2
            return binary_str

        for i in range(1, n + 1):
            if DecimalToBinary(i) not in s:
                return False
        return True
         