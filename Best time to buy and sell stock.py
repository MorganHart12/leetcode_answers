class Solution(object):
    def maxProfit(self, prices):
        maxprofit = 0
        
        for y in range(len(prices)):
            for x in range (1, len(prices)):
                if prices[x] > prices[y]:
                    profit = prices[x] - prices[y]
                    max(maxprofit, profit)
                else: 
                    y += 1

        return maxprofit
