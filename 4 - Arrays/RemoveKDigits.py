class Solution:

    #   Time:   O(N) --> a max of double visit 
    #   Space:  O(N)

    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []
        
        #   before pushing a digit to stack, take care that it is monotonically increasing stack, also k > 0 and stack not empty
        for i in range(len(num)):
            
            currentNumber = int(num[i])
            
            while (len(stack) > 0 and k > 0 and currentNumber < stack[-1]):
                stack.pop()
                k -= 1
                
            stack.append(currentNumber)
        
        #   as stack is monotonically increasing => we can pop all lastly added elements until k <= 0   
        while (k > 0):
            stack.pop()
            k -= 1
        
        #   remove all leading zeros   
        cursor = 0
        while (cursor < len(stack)):
            if (stack[cursor] != 0):
                break
            cursor += 1
            
        stack = stack[cursor:]
        
        #   edge case
        if (len(stack) == 0):
            return '0'
        
        #   now join the stack again
        return ''.join([str(n) for n in stack])