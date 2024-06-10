class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list1=[]
        set1
        for n in nums1:
            if n in nums2 and n not in list1:
                list1.append(n)
        return list1