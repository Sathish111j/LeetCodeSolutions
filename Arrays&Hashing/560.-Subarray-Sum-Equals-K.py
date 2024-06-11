class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result=0
        currSum=0
        prefix={0:1}

        for num in nums:
            currSum+=num
            difference=currSum-k

            result+=prefix.get(difference,0)

            prefix[currSum]=1+prefix.get(currSum,0)
        return result