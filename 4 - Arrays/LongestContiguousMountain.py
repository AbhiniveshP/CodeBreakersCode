class Solution:

    #   Time:   O(N)
    #   Space:  O(1)
    def longestMountain(self, A: List[int]) -> int:
        
        #   initialize start which actually moves from mountain start to the next mountain start
        #   end pointer which moves from start of a mountain to end of a mountain keeping start pointer static
        #   maximum mountain length to keep it updated
        maxMountainLength = 0
        startIndex = 0
        endIndex = 0
        n = len(A)
        
        #   iterate until start pointer reaches end (this will happen if end pointer reaches end as well)
        while (startIndex < n):
            
            #   reset end pointer to the new mountain start pointer
            endIndex = startIndex
            
            #   if the end is within bounds and belongs to increasing mountain part, then only do the following
            if (endIndex + 1 < n and A[endIndex] < A[endIndex + 1]):
                
                #   first move the end till the peak
                while (endIndex + 1 < n and A[endIndex] < A[endIndex + 1]):
                    endIndex += 1
                
                #   once peak is reached, if the end can have to downhill, then only do the following 
                if (endIndex + 1 < n and A[endIndex] > A[endIndex + 1]):

                    #   now move till end of the mountain
                    while (endIndex + 1 < n and A[endIndex] > A[endIndex + 1]):
                        endIndex += 1
                    
                    #   update max mountain length     
                    maxMountainLength = max(maxMountainLength, endIndex - startIndex + 1)
            
            #   update start to next index if not mountain, or update start index to the end of the mountain if mountain
            startIndex = max(endIndex, startIndex + 1)
            
        #   return max length    
        return maxMountainLength                   
                    