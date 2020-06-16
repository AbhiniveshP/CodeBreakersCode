class Solution:
    
    #   Time Complexity:    O(n^2)
    #   Space Complexity:   O(1)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #   edge cases
        if (nums == None or len(nums) < 3):
            return []
        
        finalOutput = []
        
        #   sort the array
        nums.sort()
        
        #   use 3-pointer technique while fixing one pointer and moving two other pointers
        for first in range(len(nums) - 2):
            
            #   a duplicate case check
            if (first != 0 and nums[first] == nums[first - 1]):
                continue
            
            second = first + 1
            third = len(nums) - 1
            
            #   move second and third pointers accordingly
            while (second < third):
                
                currentSum = nums[first] + nums[second] + nums[third]
                
                if (currentSum < 0):
                    second += 1
                    
                elif (currentSum > 0):
                    third -= 1
                    
                else:
                    finalOutput.append( [ nums[first], nums[second], nums[third] ] )
                    second += 1
                    third -= 1
                    
                    #   move until you find non-duplicate for both second and third pointers
                    while (second < third and nums[second] == nums[second - 1]):
                        second += 1
                        
                    while (second < third and nums[third] == nums[third + 1]):
                        third -= 1
                        
        return finalOutput