class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        #   edge case check
        if (nums == None or len(nums) == 0):
            return True
        
        totalSum = sum(nums)

          # if totalSum is an odd number, we can't have two subsets with same total
        if (totalSum % 2 != 0):
            return False
        
        sumToForm = totalSum // 2
        
        #   initializations
        canPartDP = [ [ False for col in range(sumToForm + 1) ] for row in range(len(nums)) ]
        
        #   populate the sum=0 column, as we can always have '0' sum without including any element
        for row in range(len(nums)):
            canPartDP[row][0] = True
        
        #   with only one number, we can form a subset only when the required sum is equal to its value
        for col in range(1, sumToForm + 1):
            if (col == nums[0]):
                canPartDP[0][col] = True
                
        #   process all subsets for all sums
        for arrayIndex in range(1, len(nums)):
            for currentSum in range(1, sumToForm + 1):
                
                #   opt 2 is current element not included
                opt1, opt2 = False, canPartDP[arrayIndex - 1][currentSum]
                
                #   opt 1 is current element included only if less than target sum
                if (currentSum >= nums[arrayIndex]):
                    opt1 = canPartDP[arrayIndex - 1][currentSum - nums[arrayIndex]]
                
                #   perform OR between both the options   
                canPartDP[arrayIndex][currentSum] = opt1 or opt2
        
        #   return the last cell which tells whether we can have a subset with half sum
        return canPartDP[len(nums)-1][sumToForm]
                    