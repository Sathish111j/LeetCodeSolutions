class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counters = [Counter(w) for w in words2]
        max_counter = Counter()
        for c in counters:
            for key, val in c.items():
                max_counter[key] = max(max_counter[key], val)

        res = []
        for word in words1:
            c = Counter(word)
            if max_counter <= c: # we can compare hashmap like the comapre the common keys
                res.append(word)
        return res