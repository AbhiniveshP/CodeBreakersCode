class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        #   edge case check
        if (s == None or len(s) == 0):
            return 0
        
        #   LPS[i][j] stores the length of LPS from index 'i' to index 'j'
        LPS = [ [ 0 for c in range(len(s)) ] for r in range(len(s)) ]
        
        #   every sequence with one element is a palindrome of length 1
        for i in range(len(s)):
            LPS[i][i] = 1
            
        for startIndex in range(len(s)-1, -1, -1):
            for endIndex in range(startIndex+1, len(s)):
                
                #   case 1: elements at the beginning and the end are the same
                if (s[startIndex] == s[endIndex]):
                    LPS[startIndex][endIndex] = 2 + LPS[startIndex + 1][endIndex - 1]
                
                #   case 2: skip one element either from the beginning or the end    
                else:
                    LPS[startIndex][endIndex] = max(LPS[startIndex + 1][endIndex],
                                                   LPS[startIndex][endIndex - 1])
                    
        return LPS[0][len(s)-1]