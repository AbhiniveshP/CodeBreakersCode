class Solution:
    
    #   Time:   O(2^N)
    #   Space:  O(2^N)
    def __helper(self, nums: List[int], currentIndex: int, tempList: List[int], subSetsList: List[List[int]]) -> None:
        
        #   add whenever this funcction is called
        subSetsList.append(list(tempList))
        
        #   iterate from current index to last index,
        #   add the iterating index's value to temp list and backtrack once done.
        for secondIndex in range(currentIndex, len(nums)):
            tempList.append(nums[secondIndex])
            self.__helper(nums, secondIndex + 1, tempList, subSetsList)
            tempList.pop()
            
        return
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        if (nums == None or len(nums) == 0):
            return[]
        
        subSetsList = []
        
        self.__helper(nums, 0, [], subSetsList)
        
        return subSetsList