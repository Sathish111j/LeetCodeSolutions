class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = {}
        for item in nums:
            if item in frequency:
                frequency[item] += 1
            else:
                frequency[item] = 1
                
        def bubble_sort(arr):
            n = len(arr)
            for i in range(n):
                for j in range(0, n-i-1):
                    if (frequency[arr[j]], -arr[j]) > (frequency[arr[j+1]], -arr[j+1]):#tuple comparision wehn the 1st elem in  tuple is same then compare sthe second element
                        arr[j], arr[j+1] = arr[j+1], arr[j]
            return arr

        sorted_nums = bubble_sort(nums)
        
        # frequency = Counter(nums)
        # sorted_nums = sorted(nums, key=lambda x: (frequency[x], -x))
        

        return sorted_nums

