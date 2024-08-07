#similar to finding the lower bound of the element in the sorted array

def searchInsert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return  left    # this can be done with having an ands variable like lower bound but this left always points to the index where the target should be insertedwhen it termiantes the loop    
