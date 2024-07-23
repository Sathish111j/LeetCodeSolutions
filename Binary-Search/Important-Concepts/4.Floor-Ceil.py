# when the number is there then the floor and ceil are the same

def floor(arr, target):
    left, right = 0, len(arr) - 1
    ans = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] <= target:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans

def ceil(arr, target):
    left, right = 0, len(arr) - 1
    ans = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            ans = mid
            right = mid - 1
    return ans
