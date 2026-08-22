class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        currentMaxP = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                currentMaxP = max(currentMaxP, profit)
            else:
                buy = sell
            sell += 1
            
        return currentMaxP