class Solution:

    #   Time:   O(N)
    #   Space:  O(N)
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if (nums == None or len(nums) < 2):
            return []
        
        numberIndexMap = {}
        
        for i in range(len(nums)):
            
            complimentNumber = target - nums[i]
            
            if (complimentNumber in numberIndexMap):
                return [ numberIndexMap[complimentNumber], i ]
            
            numberIndexMap[ nums[i] ] = i
            
        return []