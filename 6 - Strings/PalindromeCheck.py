class Solution:

    #   Time:   O(N)
    #   Space:  O(1)
    def isPalindrome(self, s: str) -> bool:
        
        #   edge cases
        if (s == None or len(s) < 2):
            return True
        
        first = 0
        last = len(s) - 1
        
        while (first < last):
            
            #   move first and last pointers until a valid char
            while (first < last and not s[first].isalnum()):
                first += 1
                
            while (first < last and not s[last].isalnum()):
                last -= 1
                
            if (first < last and s[first].lower() != s[last].lower()):
                return False
            
            first += 1
            last -= 1
            
        return True