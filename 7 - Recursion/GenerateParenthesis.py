class Solution:
    
    #   Time:   O(N^N)
    #   Space:  O( (N^N) * N)

    def __helper(self, n: int, currentLength: int, partialStr: str, visitedStrs: set, finalStrings: List[str]) -> None:
        
        #   if you reach last index => all are valid candidates once reached here
        if (currentLength == n):
            finalStrings.append(partialStr)
            return
        
        #   iterate until the last index, generate new string and backtrack only if not already occurred
        for index in range(len(partialStr) + 1):
            newStr = partialStr[:index] + '()' + partialStr[index:]
            if (newStr not in visitedStrs):
                visitedStrs.add(newStr)
                self.__helper(n, currentLength + 1, newStr, visitedStrs, finalStrings)
        
        return
    
    def generateParenthesis(self, n: int) -> List[str]:
        
        if (n <= 0):
            return []
        
        finalStrings = []
        
        self.__helper(n, 0, '', set(), finalStrings)
        
        return finalStrings