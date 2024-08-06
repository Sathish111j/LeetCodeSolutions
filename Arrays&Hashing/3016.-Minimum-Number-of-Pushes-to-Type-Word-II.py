class Solution:
    def minimumPushes(self, word: str) -> int:
        words = list(word)
        frequency = Counter(words)

        frequencySort = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

        mapping = {}

        for i, (char, _) in enumerate(frequencySort):
            if i <=7:
                mapping[char] = 1
            elif i <= 15:
                mapping[char] = 2
            elif i <= 23:
                mapping[char] = 3
            else:
                mapping[char] = 4
                
        res = 0
        for w in word:
            res += mapping[w]
        
        return res



        