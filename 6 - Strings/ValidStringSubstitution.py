class Solution:

    #   Time:   O(N)
    #   Space:  O(N)
    def isValid(self, S: str) -> bool:
        
        #   edge cases
        if (S == None or len(S) < 3):
            return False
        
        stack = []
        
        #   for each char, push it to stack. Once the top 3 elements are abc => pop all 3 => trying to make (X + abc + Y)
        for char in S:
            
            stack.append(char)
            
            if (len(stack) >= 3):
                if (stack[-1] == 'c' and stack[-2] == 'b' and stack[-3] == 'a'):
                    stack.pop(); stack.pop(); stack.pop()
        
        #   if stack is empty => of the form (X + abc + Y)          
        return (len(stack) == 0)