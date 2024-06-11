class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1

            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        def quicksort_inplace(arr, low, high):
            if low < high:
                pivot_index = partition(arr, low, high)
                quicksort_inplace(arr, low, pivot_index - 1)
                quicksort_inplace(arr, pivot_index + 1, high)
        quicksort_inplace(nums, 0, len(nums) - 1)
        