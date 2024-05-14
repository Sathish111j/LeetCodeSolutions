class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        if n ==1:
            return [-1]
        
        right_max=arr[-1]
        arr[-1]=-1

        for i in range (n-2,-1,-1):
            current=arr[i]
            arr[i]=right_max
            if current>right_max:
                right_max=current
        return arr
   