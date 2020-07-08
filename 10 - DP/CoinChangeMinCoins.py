class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        #   edge cases
        if (amount == 0):
            return 0
        
        if (coins == None or len(coins) == 0):
            return -1
        
        #   if not possible => inf coins required => initialize with +inf
        minCoins = [ [ float('inf') for c in range(amount + 1) ] for r in range(len(coins)) ]
        
        for r in range(len(coins)):
            minCoins[r][0] = 0
            
        for coinIndex in range(len(coins)):
            for currentAmount in range(1, amount + 1):
                
                ways1, ways2 = float('inf'), float('inf')
                
                #   don't include
                if (coinIndex >= 1):
                    ways1 = minCoins[coinIndex - 1][currentAmount]
                
                #   include (check +inf condition as well***)   
                if (currentAmount >= coins[coinIndex] and minCoins[coinIndex][currentAmount - coins[coinIndex]] != float('inf')):
                    ways2 = minCoins[coinIndex][currentAmount - coins[coinIndex]] + 1
                    
                minCoins[coinIndex][currentAmount] = min(ways1, ways2)
                
        return minCoins[-1][amount] if minCoins[-1][amount] != float('inf') else -1