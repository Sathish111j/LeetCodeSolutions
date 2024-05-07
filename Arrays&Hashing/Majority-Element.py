class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashtable = defaultdict(int)
        for num in nums:
            if num in nums:
                hashtable[num]+=1
        maxvalue=0
        maxkey=0
        for key, value in hashtable.items():
            if value>maxvalue:
                maxkey=key
                maxvalue=value
        return maxkey 


            
