class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        for i in range(len(arr)-2):
            p1=arr[i]
            p2=arr[i+1]
            p3=arr[i+2]
            if p1%2==1 and p2%2==1 and p3%2==1:
                return True
        
        return False
