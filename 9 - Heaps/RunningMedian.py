from heapq import heappush as insert
from heapq import heappop as remove

class MedianFinder:

    #   Time:   Adding => O(logN); finding => O(1)
    #   Space:  O(N)

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lowerHalfMaxHeap = []
        self.upperHalfMinHeap = []

    def addNum(self, num: int) -> None:
        
        #   if upper half min heap is empty or current element is greater than its min (=> current element's place 
        #   is definitely in upper half whereas not sure about the heap's min element).
        if ( len(self.upperHalfMinHeap) == 0 or num > self.upperHalfMinHeap[0] ):
            insert(self.upperHalfMinHeap, num)
        
        else:
            insert(self.lowerHalfMaxHeap, -num)
        
        #   re-balance according to the sizes   
        while ( abs(len(self.upperHalfMinHeap) - len(self.lowerHalfMaxHeap)) >= 2):
            
            if (len(self.upperHalfMinHeap) > len(self.lowerHalfMaxHeap)):
                number = remove(self.upperHalfMinHeap)
                insert(self.lowerHalfMaxHeap, -number)
                
            else:
                number = remove(self.lowerHalfMaxHeap)
                insert(self.upperHalfMinHeap, -number)

    def findMedian(self) -> float:
        
        #   3 conditions to find median
        if ( len(self.upperHalfMinHeap) == len(self.lowerHalfMaxHeap) and len(self.upperHalfMinHeap) != 0):
            number1 = self.upperHalfMinHeap[0]
            number2 = -self.lowerHalfMaxHeap[0]
            return (number1 + number2) / 2
        
        elif ( len(self.upperHalfMinHeap) > len(self.lowerHalfMaxHeap) ):
            return self.upperHalfMinHeap[0]
        
        else:
            return -self.lowerHalfMaxHeap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()