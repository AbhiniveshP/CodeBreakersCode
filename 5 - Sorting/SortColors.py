class Solution:

    #   Time:   O(N)
    #   Space:  O(1)

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #   edge cases
        if (nums == None or len(nums) <= 1):
            return
        
        #   initialize low, mid, high
        low = 0
        mid = 0
        high = len(nums) - 1
        
        #   iterate until high is 1 less than mid
        while (mid <= high):
            
            #   if mid is 0 => move this 0 to low and increment low as one low is sorted
            #   move mid by 1 as well because the only posssibilities for previous low would be either 0 or 1
            #   and there is definitely not a 2 as all 2s are pushed to end until we get either a 0 or a 1 from end
            if (nums[mid] == 0):
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            
            #   if mid has 1 => this index is sorted => move mid forward
            elif (nums[mid] == 1):
                mid += 1
            
            #   if mid has 2 => push this to end and bring end element to mid and decrement high because 
            #   only high index is sorted and we aren't sure about mid index.
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                
        return 