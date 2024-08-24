class Solution:
    def nearestPalindromic(self, n: str) -> str:

        def generatePalindromeFromLeft(leftHalf, isEvenLength):
            palindrome = leftHalf
            if not isEvenLength:
                leftHalf //= 10
            while leftHalf > 0:
                palindrome = palindrome * 10 + leftHalf % 10
                leftHalf //= 10
            return palindrome

        number = int(n)
        if number <= 10:
            return str(number - 1)
        if number == 11:
            return "9"

        length = len(n)
        leftHalf = int(n[: (length + 1) // 2])

        palindromeCandidates = [
            generatePalindromeFromLeft(leftHalf - 1, length % 2 == 0),  # create palindrom by incremting 1 other follow some changes similar to this
            generatePalindromeFromLeft(leftHalf, length % 2 == 0),
            generatePalindromeFromLeft(leftHalf + 1, length % 2 == 0),
            10 ** (length - 1) - 1,
            10**length + 1,
        ]

        nearestPalindrome = 0
        minDifference = float("inf")

        for candidate in palindromeCandidates:
            if candidate == number:
                continue
            difference = abs(candidate - number)
            if difference < minDifference or (
                difference == minDifference and candidate < nearestPalindrome
            ):
                minDifference = difference
                nearestPalindrome = candidate

        return str(nearestPalindrome)
