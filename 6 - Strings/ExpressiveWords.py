class Solution:
    
    #   Time:   O(n + m)
    #   Space:  O(1)

    def __canStretch(self, S: str, word: str):
        
        #   initialize two pinters, one for each string
        first, second = 0, 0
        
        #   iterate until one of them reaches their ends
        while (first < len(S) and second < len(word)):
            
            #   capture the current chars and if not equal => return false directly
            c1 = S[first]
            c2 = word[second]
            
            if (c1 != c2):
                return False
            
            runner1 = first
            runner2 = second
            
            #   move the runners until they match their previous chars
            while (runner1 < len(S) and S[runner1] == c1):
                runner1 += 1
                
            while (runner2 < len(word) and word[runner2] == c2):
                runner2 += 1
            
            #   find out the stretch in each strings   
            stretch1 = runner1 - first
            stretch2 = runner2 - second
            
            #   the conditions which are not valid
            if ( (stretch1 < stretch2) or (stretch1 < 3 and stretch1 != stretch2) ):
                return False
            
            #   update the main pointers to correct positions which are same as where the runners stopped
            first = runner1
            second = runner2
        
        #   if both the main pointers are equal to their lengths => return True   
        if (first == len(S) and second == len(word)):
            return True
        
        return False
                
    
    def expressiveWords(self, S: str, words: List[str]) -> int:
        
        #   calculating count w.r.t each word
        count = 0
        
        for word in words:
            if (self.__canStretch(S, word)):
                count += 1
                
        return count