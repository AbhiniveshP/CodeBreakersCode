from collections import deque

class Solution:
    
    #   Time Complexity:    O(N + M)
    #   Space Complexity:   O(N + M)
    #   use a queue to convert from int to string
    def __getInt(self, num: str) -> int:
        
        finalNumber = 0
        
        for char in num:
            
            currentDigit = ord(char) - ord('0')
            finalNumber = finalNumber * 10 + currentDigit
        
        return finalNumber
    
    def __getStr(self, num: int) -> str:
        
        finalStr = deque([])
        
        while (num > 0):
            digit = num % 10
            num = (num // 10)
            finalStr.appendleft(chr(digit + ord('0')))
        
        if (len(finalStr) == 0):
            finalStr.append('0')
        
        return ''.join(finalStr)
        
    
    def multiply(self, num1: str, num2: str) -> str:
        
        n1 = self.__getInt(num1)
        n2 = self.__getInt(num2)
        
        return self.__getStr(n1 * n2)