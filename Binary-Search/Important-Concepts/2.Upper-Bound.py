#for finding the upper bound of the element in the sorted array
# always initiale the ans with len(arr)

def upper_bound(arr, target):
    ans = len(arr)
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] > target: # only change is here from lower bound > instead of >=
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans

#time complexity is O(logn)