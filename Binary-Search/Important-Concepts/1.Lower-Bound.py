#this is for finding the lower bound of the element in the  sorted array with or without duplicates
# always initiale the ans with  len(arr)
def lower_bound(arr, target):
    ans = len(arr)
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] >= target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans

#time complexity is O(logn)