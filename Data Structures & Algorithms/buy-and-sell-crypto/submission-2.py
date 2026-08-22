class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        print(len(prices))
        if len(prices) == 1:
            return 0

        for i in range(len(prices) - 1):
            buy = prices[i]

            for j in range(i+1, len(prices)):
                sell = prices[j]
                profit = sell - buy

                profits.append(profit)
        
        print(profits)
        max_profit = max(profits)
        if max_profit >= 0:
            return max_profit
        else:
            return 0
                
        
        

            
        
