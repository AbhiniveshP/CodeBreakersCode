from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordSet = set(wordList)
        
        queue = deque([beginWord])
        level = 1
        
        if (endWord not in wordSet):
            return 0
        
        while (len(queue) > 0):
            
            levelSize = len(queue)
            
            for i in range(levelSize):
                currentWord = queue.popleft()
                
                for k in range(len(currentWord)):
                    
                    for j in range(26):
                        newChar = chr(ord('a') + j)
                        
                        if (newChar != currentWord[k]):
                            newWord = currentWord[:k] + newChar + currentWord[k+1:]
                            
                            if (newWord in wordSet):
                                
                                if (newWord == endWord):
                                    return level + 1
                                
                                queue.append(newWord)
                                wordSet.remove(newWord)
                                
            level += 1
                
        return 0