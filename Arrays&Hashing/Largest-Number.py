class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def compare(x, y):
            return int(y + x) - int(x + y) 
    
        nums_str = [str(num) for num in nums] #num to str
        
        nums_str.sort(key=functools.cmp_to_key(compare)) #sort it

        if nums_str[0] == "0": # special case when zero is largest  number
            return "0"

        return "".join(nums_str)

#Time complexity: O(nlogn)