class Solution:
	#	Time Complexity:	O(n)
	#	Space Complexity:	O(1)

    def removeDuplicates(self, nums: List[int]) -> int:
        
        #	edge case check
        if (nums == None or len(nums) == 0):
            return 0
        
        #	maintain two pointers slow and fast,
        #	slow moves forward only when num at fast != num at slow
        slow = 0
        
        for fast in range(1, len(nums)):
            
            if (nums[fast] != nums[slow]):
                slow += 1
                nums[slow] = nums[fast]
        
        #	return the number where slow is currently at       
        return slow + 1