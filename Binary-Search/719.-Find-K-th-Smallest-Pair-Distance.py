class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # dist=[]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #             dist.append(abs(nums[i]-nums[j]))
        
        # dist.sort()

        # return dist[k-1] #TLE

        def countPairsWithInDistance(dist):
            left=0
            count=0
            for right in range(len(nums)):
                while nums[right]-nums[left]>dist:
                    left+=1
                count+=right-left
            return count
    
        nums.sort()
        low=0
        high=nums[-1]-nums[0]

        while low<high:
            mid=low+(high-low)//2
            if countPairsWithInDistance(mid)<k:
                low=mid+1
            else:
                high=mid
        return low


