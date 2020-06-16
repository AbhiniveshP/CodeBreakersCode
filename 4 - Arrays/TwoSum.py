class Solution:
    #   Time Complexity:    O(n)
    #   Space Complexity:   O(n)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #   edge cases
        if (nums == None or len(nums) < 2):
            return []
        
        #   maintain a HashMap of number: index as indices have to be returned
        numberIndexMap = {}
        
        #   check if compliment of current number exists
        #   if exists => return both indices
        #   else => add current number and its index to the HashMap
        for i in range(len(nums)):
            
            complimentNumber = target - nums[i]
            
            if (complimentNumber in numberIndexMap):
                return [ numberIndexMap[complimentNumber], i ]
            
            numberIndexMap[ nums[i] ] = i
            
        return []