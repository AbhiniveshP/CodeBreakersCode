class Solution:

	#	Time:	O(N)
	#	Space:	O(1)
    def fib(self, N: int) -> int:
        
        if (N <= 1):
            return N
        
        f1, f2 = 0, 1
        
        for i in range(2, N + 1):
            result = f1 + f2
            f1 = f2
            f2 = result
            
        return result