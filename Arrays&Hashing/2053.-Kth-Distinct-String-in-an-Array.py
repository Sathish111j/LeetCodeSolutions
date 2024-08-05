class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # index={}

        # for i in range(len(arr)):
        #     if arr[i] in index:
        #         index[arr[i]]=-1
        #     else:
        #         index[arr[i]]=i

        # distinct = [item for item in index.items() if item[1] != -1]
        # sortedDistinct = sorted(distinct, key=lambda x: x[1])
        
        # if k <= len(sortedDistinct):
        #     return sortedDistinct[k-1][0]
        # else:
        #     return ""

        index={}

        for i in range(len(arr)):
            if arr[i] in index:
                index[arr[i]]+=1
            else:
                index[arr[i]]=1
        c=""
        n=0
        for i,j in index.items():
            if j==1:
                c=i
                n+=1
            if n==k:
                return i
        return ""