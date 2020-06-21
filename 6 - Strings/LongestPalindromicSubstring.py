class Solution:
    
    #   Time:   O(N^2)
    #   Space:  O(1)

    def __init__(self):
        self.start = 0
        self.maxLen = 0
    
    def __getLongestFromMiddle(self, s: str, left: int, right: int) -> None:
        
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        
        #   don't forget to move back left and right pointers   
        left += 1
        right -= 1
        
        currentLength = right - left + 1
        
        #   update start and max lengths
        if (currentLength > self.maxLen):
            self.start = left
            self.maxLen = currentLength
            
        return
    
    def longestPalindrome(self, s: str) -> str:
        
        if (s == None or len(s) < 2):
            return s
        
        for middle in range(len(s)):
            self.__getLongestFromMiddle(s, middle, middle)
            self.__getLongestFromMiddle(s, middle, middle+1)
            
        return s[self.start : self.start + self.maxLen]