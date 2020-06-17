class Solution:

    #   Time Complexity:    O(n)
    #   Space Complexity:   O(1)
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #   edge case checks
        if (s == None or len(s) == 0):
            return 0
        
        #   we can apply sliding window technique
        maxLength = 1
        start = 0
        elementsPresent = set([s[0]])
        
        #   move start and end until there is no duplicate and update max length accordingly
        for end in range(1, len(s)):
            
            while (start <= end and s[end] in elementsPresent ):
                elementsPresent.remove(s[start])
                start += 1
                
            elementsPresent.add(s[end])
                
            maxLength = max(maxLength, end - start + 1)
                
        return maxLength