class Solution:

    #   Time Complexity:    O(n)
    #   Space Complexity:   O(1)
    
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        #   edge case checks
        if (nums == None or len(nums) == 0 or k == 0):
            return 0
        
        #   the main condition given is that all integers are positive, we can apply sliding window technique
        slow = -1
        currentProduct = 1
        finalCount = 0
        
        #   update final count by fast-slow which gives number of extra subarrays added to the final count
        for fast in range(len(nums)):
            
            currentProduct *= nums[fast]
            
            while (slow < fast and currentProduct >= k):
                slow += 1
                currentProduct = int(currentProduct / nums[slow])
                
            finalCount += (fast - slow)
            
        return finalCount