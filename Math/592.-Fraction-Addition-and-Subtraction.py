class Solution:
    def fractionAddition(self, expression: str) -> str:
        def parseFraction(s):
            sign = 1
            if s[0] == '-':
                sign = -1
                s = s[1:]
            elif s[0] == '+':
                s = s[1:]
            
            numerator, denominator = map(int, s.split('/'))
            return sign * numerator, denominator

        fractions = []
        i = 0
        while i < len(expression):
            if expression[i] in "+-":
                j = i + 1
            else:
                j = i
            while j < len(expression) and expression[j] not in "+-":
                j += 1
            fractions.append(parseFraction(expression[i:j]))
            i = j
        
        numerator = 0
        denominator = 1
        for num, denom in fractions:
            denominator = denominator * denom // gcd(denominator, denom)
        
        for num, denom in fractions:
            numerator += num * (denominator // denom)
        
        commonGcd = gcd(abs(numerator), denominator)
        numerator //= commonGcd
        denominator //= commonGcd
        
        return f"{numerator}/{denominator}"