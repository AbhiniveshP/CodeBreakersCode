class Solution:

    #   Time:   O(NlogN)
    #   Space:  O(1) --> excluding recursive stack space
    
    def __partition(self, nums: List[int], start: int, end: int) -> int:
        
        #   initializations
        pivotElement = nums[start]
        
        lo = start + 1
        hi = end
        
        #   iterate until hi becomes 1 less than lo [ended hi index is important for swapping with pivotElement]
        while (lo <= hi):
            
            #   if both are out-of-place => swap
            #   else => move lo, hi accordingly until they get out-of-place
            if (nums[lo] >= pivotElement):
                
                if (nums[hi] < pivotElement):
                    nums[lo], nums[hi] = nums[hi], nums[lo]
                    lo += 1
                    hi -= 1
                
                else:
                    hi -= 1
                    
            else:
                lo += 1
        
        #   swap hi with start index as hi index will be the correct index for pivotElement to be placed.       
        nums[hi], nums[start] = nums[start], nums[hi]
        
        return (hi)
    
    def __quickSort(self, nums: List[int], start: int, end: int) -> None:
        
        if (start >= end):
            return
        
        pivotIndex = self.__partition(nums, start, end)
        
        self.__quickSort(nums, start, pivotIndex - 1)
        self.__quickSort(nums, pivotIndex + 1, end)
        
        return
    
    def sortArray(self, nums: List[int]) -> List[int]:
        
        self.__quickSort(nums, 0, len(nums) - 1)
        return nums