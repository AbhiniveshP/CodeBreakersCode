'''
Time Complexity: O(n)
Space Complexity: O(n)
'''

class RPN:
    
    def __compute(self, num1, num2, operator):
        
        if (operator == '+'):
            return num1 + num2
        
        elif (operator == '-'):
            return num1 - num2
        
        elif (operator == '*'):
            return num1 * num2
        
        else:
            return int(num1 / num2)
    
    def evalRPN(self, tokens: List[str]) -> int:
        
        #   edge case check
        if (tokens == None or len(tokens) == 0):
            return 0
        
        #   store the set of operators in a set
        operators = set([ '+', '-', '*', '/' ])
        
        #   initialize stack
        stack = []
        
        #   for each token, perform the valid task
        for token in tokens:
            
            #   if the token is an operator => pop top 2 numbers, perform the corresponding operation and
            #   then push the result to the stack
            if (token in operators):
                
                num2 = stack.pop()
                num1 = stack.pop()
                
                #   helper function to perform the corresponding operation
                newNumber = self.__compute(num1, num2, token)
                
                stack.append(newNumber)
            
            #   if the token is a number => directly push it to the stack    
            else:
                stack.append(int(token))
         
        #   return the value remaining in the stack       
        return stack[0]