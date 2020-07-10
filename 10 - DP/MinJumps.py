class Solution:
    def jump(self, nums: List[int]) -> int:
        
        #   DP --> O(n^2) --> TLE
        if (nums == None or len(nums) == 0):
            return 0
        
        minJumps = [ float('inf') for i in range(len(nums)) ]
        minJumps[0] = 0
        
        for start in range( len(nums) - 1 ):
            end = start + 1
            while ( end < len(nums) and end <= start + nums[start] ):
                minJumps[end] = min( minJumps[end], 1 + minJumps[start] )
                end += 1
                
        return minJumps[-1]


class Solution:
    def jump(self, nums: List[int]) -> int:
        
        #   edge case check
        if (nums == None or len(nums) < 2):
            return 0
        
        #   initializations
        jumps = 0           #   aka levels
        scope = 0           #   maximum reach for a particular level that is under processing
        farthest = 0        #   farthest jumps that can be reached at any point of time
        
        #   iterate the array
        for i in range(len(nums)):
            
            #   update farthest for each index and return if it reaches or exceeds last index
            farthest = max(farthest, i + nums[i])
            
            #   don't forget to return +1 to jumps
            if (farthest >= len(nums) - 1):
                return (jumps + 1)
            
            #   if index is at maximum reach of a level => increment level and maximum reach  
            if (i == scope):
                scope = farthest
                jumps += 1
           
        return (jumps)