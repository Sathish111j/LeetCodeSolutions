class Solution:
    def nthUglyNumber(self, n: int) -> int:
        primes = [2,3,5]
        uglyHeap = [1]
        visited = set()
        visited.add(1)
        for _ in range(n):
            curr = heappop(uglyHeap)
            for prime in primes:
                newUgly = curr * prime
                if newUgly not in visited:
                    heappush(uglyHeap, newUgly)
                    visited.add(newUgly)
        return curr 