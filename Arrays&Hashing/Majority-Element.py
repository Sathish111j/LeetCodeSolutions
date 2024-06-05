class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hashtable = defaultdict(int)
        # for num in nums:
        #     hashtable[num]+=1
        # maxvalue=0
        # maxkey=0
        # for key, value in hashtable.items():
        #     if value>maxvalue:
        #         maxkey=key
        #         maxvalue=value
        # return maxkey 

        count=0
        ans=None

        for num in nums :
            if count ==0:
                ans=num
            if num ==ans :
                count+=1
            else :
                count-=1
        
        return ans


            
