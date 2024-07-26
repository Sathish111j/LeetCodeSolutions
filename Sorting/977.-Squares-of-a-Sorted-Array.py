class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r=0,len(nums)-1

        while r>=0:
            lSquare=(nums[l])**2
            rSquare=(nums[r])**2

            if lSquare<rSquare:
                nums[r]=rSquare
                r-=1
            else:
                nums[l]=nums[r]
                nums[r]=lSquare
                r-=1
        nums.sort()
        return nums


        # def mergeSort(nums):

        #     if len(nums)<=1:
        #         return [nums[0]**2]

        #     mid=len(nums)//2
        #     left=nums[:mid]
        #     right=nums[mid:]

        #     leftSorted=mergeSort(left)
        #     rightSorted=mergeSort(right)


        #     combined=[]
        #     i,j=0,0
        #     while i<len(leftSorted) and j <len(rightSorted):
        #         if leftSorted[i]<rightSorted[j]:
        #             combined.append(leftSorted[i])
        #             i+=1
        #         else:
        #             combined.append(rightSorted[j])
        #             j+=1
            
        #     if leftSorted:
        #         combined+=leftSorted[i:]
        #     if rightSorted:
        #         combined+=rightSorted[j:]
            
        #     return combined
        
        # return mergeSort(nums)
                