#o(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[] for i in range(len(nums)+1)]

        result=[]

        for ele in nums:
            count[ele]=1+count.get(ele,0)
        
        for n,m in count.items():
            freq[m].append(n)
        
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
