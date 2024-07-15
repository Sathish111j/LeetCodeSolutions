class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)>len(nums2):
            return self.find(nums1,nums2)
        else:
            return self.find(nums2,nums1)

    def find(self,nums1,nums2):
        hashmap={}
        for n in nums1:
            if n in hashmap:
                hashmap[n]+=1
            else:
                hashmap[n]=1
        result=[]
        for k in nums2:
            if k in hashmap and hashmap[k]!=0:
                result.append(k)
                hashmap[k]-=1

        return result

        