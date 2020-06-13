'''
Time Complexity: 	O(n)
Space Complexity:	O(n)
'''


from collections import deque

class RecentCounter:

	#	initialize a queue
    def __init__(self):
        self.__queue = deque([])

    def ping(self, t: int) -> int:
        
        #	add current timestamp to the queue
        self.__queue.append(t)
        
        #	remove all elements from the queue from the front until the timestamp of first element in queue
        #	and the latest added timestamp is less than 3000
        while (t > self.__queue[0] + 3000):
            self.__queue.popleft()
        
        #	once all unnecessary timestamps from the front are removed
        #	=> return the number of remaining timestamps in the queue   
        return len(self.__queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)