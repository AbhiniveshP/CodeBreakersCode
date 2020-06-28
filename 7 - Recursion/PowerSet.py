class Solution:
    
    #   Time:   O(2^N)
    #   Space:  O(2^N)
    def __helper(self, nums: List[int], prevIndex: int, tempList: List[int], finalLists: List[List[int]]) -> None:
        
        #   each candidate that we pass as an argument (tempList) is a valid candidate => add the candidate
        finalLists.append(tempList[:])
        
        #   list of possible candidates are from next index of passed index to the last index
        for indexToAdd in range(prevIndex + 1, len(nums)):
            tempList.append(nums[indexToAdd])
            self.__helper(nums, indexToAdd, tempList, finalLists)
            tempList.pop()
            
        return
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        if (nums == None or len(nums) == 0):
            return []
        
        finalLists = []
        
        self.__helper(nums, -1, [], finalLists)
        
        return finalLists