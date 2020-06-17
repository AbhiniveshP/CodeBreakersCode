class Solution:

	#   Time Complexity:    O(n)
    #   Space Complexity:   O(1)

    def maxProfit(self, prices: List[int]) -> int:
        
        #	maxProfit is nothing but the sum of positive slopes
        profitTillIndex = 0
        
        for i in range(1, len(prices)):
            profitTillIndex = profitTillIndex + ( max(prices[i] - prices[i - 1], 0) )
            
        return profitTillIndex