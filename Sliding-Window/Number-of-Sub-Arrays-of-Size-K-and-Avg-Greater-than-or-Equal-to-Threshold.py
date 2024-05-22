class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res=0
        window_sum=sum(arr[:k-1])

        for l in range(len(arr)-k+1):
            window_sum+=arr[l+k-1]
            if window_sum/k>=threshold:
                res+=1
            window_sum-=arr[l]
        return res
