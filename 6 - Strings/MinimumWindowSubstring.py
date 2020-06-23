class Solution:

    #   Time:   O(n) ==> at most traverse 2 times on main string
    #   Space:  O(n + m) 
    def minWindow(self, s: str, t: str) -> str:
        
        #   edge cases
        if (s == None or t == None or len(s) == 0 or len(t) == 0):
            return ''
        
        #   initialize two pointers for iteration, also two more for storing the optimal indices
        left, right = 0, 0
        minLeft, minRight = 0, 0
        
        #   store the frequencies of T in a hashmap
        countT = len(t)
        mapT, mapS = {}, {}
        
        for char in t:
            if (char not in mapT):
                mapT[char] = 1
            else:
                mapT[char] += 1
        
        #   store current length formed using two pointers left and right        
        minWindowSize = len(s) + 1
        currentLength = 0
        
        #   iterate until left is <= right and right is < len(S)       
        while (left <= right and right < len(s)):
            
            #   update mapS using the right pointer no matter what and stop temporarily when current length is completely formed.
            currentChar = s[right]
            if (currentChar not in mapS):
                mapS[currentChar] = 1
            else:
                mapS[currentChar] += 1
                
            if (currentChar in mapT and mapS[currentChar] <= mapT[currentChar]):
                currentLength += 1
                
            right += 1
            
            #   now work on contracting left pointer
            while (currentLength >= countT):
                
                #   current window size and updating left and right pointers
                windowSize = right - left
                if (windowSize < minWindowSize):
                    minWindowSize = windowSize
                    minLeft = left
                    minRight = right
                
                #   update mapS again now using right pointer and also decrement current length formed
                leftChar = s[left]
                mapS[leftChar] -= 1
                
                left += 1
                
                if (leftChar in mapT and mapS[leftChar] < mapT[leftChar]):
                    currentLength -= 1
        
        #   return the requirements according to the question.                     
        if (minWindowSize > len(s)):
            return ''
        return s[minLeft : minRight]