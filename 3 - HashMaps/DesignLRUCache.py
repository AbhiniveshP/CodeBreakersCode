class Node:
    
    #   Double Linked List Node structure
    def __init__(self, key, value):
        
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    #   all possible initializations --> take care to assign head to tail and tail to head
    def __init__(self, capacity: int):
        
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.maxCapacity = capacity
        self.cache = {}
        
    def __insertAtHead(self, node):
        
        #   O(1) operation

        #   first step --> attach node connections properly
        node.next = self.head.next
        node.prev = self.head
        
        #   second step --> attach previous head and current head properly
        self.head.next = node
        node.next.prev = node
        
    def __remove(self, node):
        
        #   O(1) operation

        #   take in a temp node for the next possible node of current node; remove the current node connections properly
        nextNode = node.next
        node.next.prev = node.prev
        node.prev.next = nextNode

    def get(self, key: int) -> int:
        
        #   O(1) operation

        # if key not in cache => return -1 as it is not present in DLL
        if (key not in self.cache):
            return -1
        
        #   otherwise, remove the current node and insert at the front
        currentNode = self.cache[key]
        
        self.__remove(currentNode)
        self.__insertAtHead(currentNode)
        
        #   return the corresponding value
        return currentNode.value
        

    def put(self, key: int, value: int) -> None:
        
        #   O(1) operation

        #   if key is already present => update the new value; remove it and insert at front
        if (key in self.cache):
            
            currentNode = self.cache[key]
            currentNode.value = value
            
            self.__remove(currentNode)
            self.__insertAtHead(currentNode)
            return
        
        #   otherwise => insert the new value at the front, add it to cache, check the size of cache and remove the last node if size exceeds
        newNode = Node(key, value)
        self.cache[key] = newNode
        
        self.__insertAtHead(newNode)
        self.size += 1
        
        if (self.size > self.maxCapacity):
            
            lastNode = self.tail.prev
            self.__remove(lastNode)
            del self.cache[lastNode.key]
            self.size -= 1
            
        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)