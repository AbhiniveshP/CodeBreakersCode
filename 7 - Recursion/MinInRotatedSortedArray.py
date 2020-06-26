class Solution:

    #   Time:   O(logN)
    #   Space:  O(1)
    def findMin(self, nums: List[int]) -> int:
        
        lo = 0
        hi = len(nums) - 1
        
        if (len(nums) == 1):
            return nums[0]
        
        #   array not rotated
        if (nums[hi] > nums[lo]):
            return nums[lo]
        
        #   until lo doesn't completely cross hi
        while (lo <= hi):
            
            mid = lo + int( (hi - lo) / 2) 
            
            # if the mid element is greater than its next element, then mid+1 element is the smallest
            # This point would be the point of change. From higher to lower value.
            if (nums[mid] > nums[mid + 1]):
                return nums[mid + 1]
            
            # if the mid element is lesser than its previous element, then mid element is the smallest
            if (nums[mid] < nums[mid - 1]):
                return nums[mid]
            
            # if the mid elements value is greater than the 0th element this means
            # the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]
            if (nums[mid] > nums[lo]):
                lo = mid + 1
            
            # if nums[0] is greater than the mid value then this means the smallest value is somewhere to the left    
            else:
                hi = mid - 1
                
        return 