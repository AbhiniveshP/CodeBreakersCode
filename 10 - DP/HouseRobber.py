class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if (nums == 0 or len(nums) == 0):
            return 0
        
        prevMax, currMax = 0, nums[0]
        
        for i in range(1, len(nums)):
            
            newMax = max(currMax, nums[i] + prevMax)
            prevMax = currMax
            currMax = newMax
            
        return currMax