class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):

            if len(nums)<=1:
                return nums

            mid=len(nums)//2
            left=nums[:mid]
            right=nums[mid:]

            leftSorted=mergeSort(left)
            rightSorted=mergeSort(right)


            combined=[]
            i,j=0,0
            while i<len(leftSorted) and j <len(rightSorted):
                if leftSorted[i]<rightSorted[j]:
                    combined.append(leftSorted[i])
                    i+=1
                else:
                    combined.append(rightSorted[j])
                    j+=1
            
            if leftSorted:
                combined+=leftSorted[i:]
            if rightSorted:
                combined+=rightSorted[j:]
            
            return combined
        
        return mergeSort(nums)

        