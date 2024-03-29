class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)

        for s in strs :
            char=[0] *26

            for c in s:
                char[ord(c)-ord("a")]+=1

            result[tuple(char)].append(s)
        return result.values()