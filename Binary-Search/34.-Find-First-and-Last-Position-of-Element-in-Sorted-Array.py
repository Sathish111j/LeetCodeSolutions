class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        

        def binarySearch(nums,isStart):
            ans=-1

            start=0
            end=len(nums)-1

            while start<=end:
                mid=start+(end-start)//2

                if target> nums[mid]:
                    start=mid+1
                elif target < nums[mid]:
                    end=mid-1
                else:
                    ans=mid
                    if isStart:
                        end=mid-1
                    else:
                        start=mid+1
            return ans

        return [binarySearch(nums,True),binarySearch(nums,False)]