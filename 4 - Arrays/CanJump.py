class Solution:

    #   Time Complexity:    O(n)
    #   Space Complexity:   O(1)

    def canJump(self, nums: List[int]) -> bool:
        
        #   edge cases
        if (nums == None or len(nums) < 2):
            return True
        
        #   maintain maxReach in a greedy way
        maxReach = 0
        
        for i in range(len(nums)):
            
            #   case for non-reachability
            if (maxReach < i):
                return False
            
            #   update maxReach
            maxReach = max(maxReach, i + nums[i])
            if (maxReach >= len(nums) - 1):
                return True
            
        return True