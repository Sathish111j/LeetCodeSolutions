class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return words[0]
        common=[]
        chars=set(words[0])

        for c in chars:
            frequency=min([word.count(c) for word in words])
            common+= frequency*[c]

        return common