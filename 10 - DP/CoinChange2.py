class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        #   edge cases
        if (coins == None):
            return 1
        
        #   edge cases
        if (len(coins) == 0):
            if (amount == 0):
                return 1
            else:
                return 0
        
        dpCoins = [ [0 for c in range(amount + 1)] for r in range(len(coins)) ]
        
        for r in range(len(coins)):
            dpCoins[r][0] = 1
            
        for coinIndex in range(len(coins)):
            for currentAmount in range(1, amount + 1):
                
                sum1, sum2 = 0, 0
                
                #   don't choose the coin
                if (coinIndex > 0):
                    sum2 = dpCoins[coinIndex - 1][currentAmount]
                
                #   choose the coin
                if (coins[coinIndex] <= currentAmount):
                    sum1 = dpCoins[coinIndex][currentAmount - coins[coinIndex]]
                    
                dpCoins[coinIndex][currentAmount] = sum1 + sum2
        
        return dpCoins[-1][amount]