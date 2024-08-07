class Solution:
    def kthElement(self, k, arr1, arr2):
        n,m=len(arr1),len(arr2)
        
        if k>m+n:
            return None
        
        i,j=0,0
        
        while i<n and j<m:
            if k==1:
                return min(arr1[i],arr2[j])
            mid=k//2
            
            mi=min(i+mid,n)-1
            mj=min(j+mid,m)-1
            
            if arr1[mi]<=arr2[mj]:
                k-=mi - i + 1
                i=mi+1
            else:
                k-=mj - j + 1
                j=mj+1
        
        if i < n:
            return arr1[i + k - 1]
        if j < m:
            return arr2[j + k - 1]
        return None