class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #merging two array without extra space merging adn puting in nums1 itself
        last=m+n-1
        while m>0 and n>0:
            if nums1[m-1]>nums2[n-1]:
                nums1[last]=nums1[m-1]
                m-=1
            else:
                nums1[last]=nums2[n-1]
                n-=1
            last -=1
        #when nums2 has left over then fill nums1 with nums2 in the same oreder
        while n>0:
            nums1[last]=nums2[n-1]
            n-=1
            last-=1
    
        