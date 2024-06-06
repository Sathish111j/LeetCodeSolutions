class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet=set(wordList)

        if endWord not in wordList:
            return 0
        
        queue=deque([(beginWord,1)])

        while queue:
            curr_word , length=queue.popleft()

            for i in range (len(curr_word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord=curr_word[:i]+c+curr_word[i+1:]

                    if newWord==endWord:
                        return length+1
                    
                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        queue.append((newWord,length+1))
        return 0
