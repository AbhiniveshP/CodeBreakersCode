class Solution:

    #   Time:   O(N) --> 2 loops at max
    #   Space:  O(1)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        #   edge cases
        if (gas == None or len(gas) == 0):
            return -1
        
        #   initialize front (which always keepd moving), rear (static and changes only if we can't start from one index)
        #   count to make sure front visits each element atmost 2 times, gas available at each instant
        front = 0
        rear = 0
        count = 0
        gasAvailable = 0
        
        #   iterate until you visit each element not more than 2 times
        while (count < 2 * len(gas)):
            
            #   if travel from current front possible => move front circularly and if front reaches rear (temporary starting point)
            if (gasAvailable + gas[front] >= cost[front]):
                
                gasAvailable += (gas[front] - cost[front])
                front = (front + 1) % len(gas)
                
                if (front == rear):
                    return front
            
            #   else => move front circularly again and make this front the new starting point (rear)
            #   also make sure to make sure gas available starts from 0 as we are starting from new index
            else:
                front = (front + 1) % len(gas)
                rear = front
                gasAvailable = 0
             
            #   increment count   
            count += 1
            
        return -1