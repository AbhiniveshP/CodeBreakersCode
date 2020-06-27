class Solution:
    
    #   Time:   O(logN)
    #   Space:  O(1)

    #   This follows template 2 of Binary Search!!!
    def __getFirst(self, nums: List[int], target: int) -> None:
        
        lo = 0
        hi = len(nums) - 1
        
        while (hi - lo >= 1):
            
            mid = lo + int( (hi - lo) / 2)
            
            if (nums[mid] == target and nums[mid - 1] != target):
                return mid
            
            if (target <= nums[mid]):
                hi = mid
                
            elif (target > nums[mid]):
                lo = mid + 1
                
        if (nums[lo] == target):
            return lo
        return -1
    
    def __getLast(self, nums: List[int], target: int) -> None:
        
        lo = 0
        hi = len(nums) - 1
        
        while (hi - lo >= 1):
            
            mid = lo + int( (hi - lo) / 2)
            
            if (nums[mid] == target and nums[mid + 1] != target):
                return mid
            
            if (target >= nums[mid]):
                lo = mid + 1
                
            elif (target < nums[mid]):
                hi = mid
                
        if (nums[lo] == target):
            return lo
        return -1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if (nums == None or len(nums) == 0):
            return [-1, -1]
        
        firstIndex = self.__getFirst(nums, target)
        lastIndex = self.__getLast(nums, target)
        
        return [firstIndex, lastIndex]