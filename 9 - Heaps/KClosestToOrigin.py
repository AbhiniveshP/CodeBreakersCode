from math import sqrt
from heapq import heappush as insert
from heapq import heappop as remove

class Point:

    #   Create a point class and override ==, <, <=, >, >= directing towards a max heap
    #   => negate distance
    
    def __init__(self, point):
        self.point = point
        self.dist = -sqrt( (point[0] ** 2) + (point[1] ** 2) )
        
    def __eq__(self, other):
        return (self.dist == other.dist)
        
    def __lt__(self, other):
        return (self.dist < other.dist)
        
    def __gt__(self, other):
        return (self.dist > other.dist)
        
    def __le__(self, other):
        return (self.dist <= other.dist)
        
    def __ge__(self, other):
        return (self.dist >= other.dist)

class Solution:

    #   Time:   O(NlogK)
    #   Space:  O(K)
    
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        minHeap = []
        
        #   once the size overloads => remove the max element from the heap
        for point in points:
            
            newPoint = Point(point)
            insert(minHeap, newPoint)
            
            if (len(minHeap) > K):
                remove(minHeap)
                
        return [each.point for each in minHeap]