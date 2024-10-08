class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        # memo={}
        # def help(ind ,prevInd):
        #     if ind==n:
        #         return 0
           
        #     if (ind,prevInd) in memo:
        #         return memo[(ind,prevInd)]

        #     length=0+help(ind+1,prevInd)

        #     if prevInd==-1 or nums[ind]>nums[prevInd]:
        #         length=max(length,1+ help(ind+1,ind))

        #     memo[(ind,prevInd)] =length

        #     return memo[(ind,prevInd)]
        # return help(0,-1)




        # dp = [[0] * (n + 1) for _ in range(n + 1)]
        # for ind in range(n - 1, -1, -1):
        #     for prevInd in range(ind - 1, -2, -1):

        #         length = 0 + dp[ind + 1][prevInd + 1]

        #         if prevInd == -1 or nums[ind] > nums[prevInd]:
        #             length = max(length, 1 + dp[ind + 1][ind + 1])

        #         dp[ind][prevInd + 1] = length

        # return dp[0][-1+1]




        # if n <= 1:
        #     return n

        # dp = [1] * n
        
        # for i in range(1, n):
        #     for j in range(i):

        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i], dp[j] + 1)

        # return max(dp)

        # hashmap=list(range(n))

        # if n <= 1:
        #     return n

        # dp = [1] * n

        # maxi = 1
        # lastIndex = 0
        
        # for i in range(1, n):
        #     hashmap[i]=i
        #     for prev in range(i):

        #        if nums[prev] < nums[i] and 1 + dp[prev] > dp[i]:
        #         dp[i] = 1 + dp[prev]
        #         hashmap[i] = prev

        #     if dp[i] > maxi:
        #         maxi = dp[i]
        #         lastIndex = i


        # lis = []
        # while hashmap[lastIndex] != lastIndex:
        #     lis.append(nums[lastIndex])
        #     lastIndex = hashmap[lastIndex]
        # lis.append(nums[lastIndex])  

        # lis.reverse()  

        # print("Longest Increasing Subsequence:", lis)
        # return maxi



        if not nums:
            return 0
        temp = []
        temp.append(nums[0])
        for i in range(1, len(nums)):

            if nums[i] > temp[-1]:
                temp.append(nums[i])

            else:
                ind = bisect_left(temp, nums[i])
                temp[ind] = nums[i]

        return len(temp)