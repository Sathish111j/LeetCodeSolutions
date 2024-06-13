# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def findPeakElement( nums):
            start=0
            end = mountain_arr.length() - 1

            while start< end:
                mid=start+(end-start)//2

                if nums.get(mid)>nums.get(mid+1):
                    end=mid
                else:
                    start=mid+1
            return start


        def binarySearch(nums, target,start,end):
            while start <=end:
                mid=start+(end-start)//2
                if target ==nums.get(mid):
                    return mid
                elif target>nums.get(mid):
                    start=mid+1
                else:
                    end=mid-1 
            return -1
        
        def OrderAgnosticBinarySearch(nums, target,start,end):
            while start <=end:
                mid=start+(end-start)//2
                if target ==nums.get(mid):
                    return mid
                elif target<nums.get(mid):
                    start=mid+1
                else:
                    end=mid-1 
            return -1
        
        peakindex=findPeakElement(mountain_arr)
        result1=binarySearch(mountain_arr,target,0,peakindex)
        if result1!=-1:
            return result1
        else:
            return OrderAgnosticBinarySearch(mountain_arr,target,peakindex+1, mountain_arr.length() - 1)


