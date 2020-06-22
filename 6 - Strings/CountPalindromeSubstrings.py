class Solution:

    #   Time:   O(N^2)
    #   Space:  O(1)
    
    def __updatePalindromeCount(self, s: str, left: int, right: int, count: List[int]) -> None:
        
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
            count[0] += 1
    
    def countSubstrings(self, s: str) -> int:
        
        count = [0]
        
        for midIndex in range(len(s)):
            
            self.__updatePalindromeCount(s, midIndex, midIndex, count)
            self.__updatePalindromeCount(s, midIndex, midIndex + 1, count)
            
        return count[0]