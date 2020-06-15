class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        #   initialize required constants
        self.hashSize = 1000
        self.array = [None for i in range(self.hashSize)]
        
    def __getHashIndex(self, key: int) -> int:
        
        #   O(1) Time
        #   return modulo value of the key
        return (key % self.hashSize)

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        
        #   O(1) average Time

        #   get the index
        index = self.__getHashIndex(key)
        
        #   create the new list if not exists 
        if (self.array[index] == None):
            self.array[index] = []
        
        #   iterate till you find key value to either edit or add it to the end   
        for innerIndex in range(len(self.array[index])):
            if (self.array[index][innerIndex][0] == key):
                self.array[index][innerIndex] = [key, value]
                return
            
        self.array[index].append([key, value])
        return
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """

        #   O(1) average Time

        #   get the index
        index = self.__getHashIndex(key)
        

        #   itertate the current index until you find the key and return the corresponding value
        if (self.array[index] == None):
            return -1
        
        for innerIndex in range(len(self.array[index])):
            if (self.array[index][innerIndex][0] == key):
                value = self.array[index][innerIndex][1]
                return value
            
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """

        #   O(1) average Time

        #   get the index
        index = self.__getHashIndex(key)
        
        #   itertate the current index until you find the key and remove the corresponding pair
        if (self.array[index] == None):
            return
        
        for innerIndex in range(len(self.array[index])):
            if (self.array[index][innerIndex][0] == key):
                currentPair = self.array[index][innerIndex]
                self.array[index].remove(currentPair)
                return
            
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)