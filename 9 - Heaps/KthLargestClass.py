from heapq import heappush as insert
from heapq import heappop as remove

class KthLargest:

    #   Time:   O(logK)
    #   Space:  O(K)

    def __init__(self, k: int, nums: List[int]):
        
        #   initialize in such a way that your Data Structure has only k largest elements
        self.minHeap = []
        self.capacity = k
        
        for num in nums:
            insert(self.minHeap, num)
            
            if (len(self.minHeap) > k):
                remove(self.minHeap)
            

    def add(self, val: int) -> int:
        
        #   first insert the new value and if size exceeds => remove the min value
        insert(self.minHeap, val)
        
        if (len(self.minHeap) > self.capacity):
            remove(self.minHeap)
        
        #   kth largest would be == first element   
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)