class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if (cost == None or len(cost) == 0):
            return 0
        
        minCostDP = [ cost[0], cost[1] ]
        
        for i in range(2, len(cost)):
            cost1, cost2 = minCostDP[i - 1], minCostDP[i - 2]
            minCostDP.append( cost[i] + min(cost1, cost2) )
        
        return min(minCostDP[-1], minCostDP[-2])