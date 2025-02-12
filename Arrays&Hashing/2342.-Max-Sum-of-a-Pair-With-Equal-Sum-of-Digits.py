class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        group=defaultdict(int)
        def sumOfDigits(n):
            sum_ = 0
            while n != 0:
                last = n % 10
                sum_ += last
                n //= 10
            return sum_

        
        maxSum=-1
        for num in nums:
            dSum=sumOfDigits(num)   # dSum = sum(map(int, str(num))) 
            if dSum in group:
                maxSum =max(maxSum,num+group[dSum])
            group[dSum]=max(group[dSum],num)

        return maxSum


            
