class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frequency=Counter(arr)
        return len(frequency.values())==len(set(frequency.values()))