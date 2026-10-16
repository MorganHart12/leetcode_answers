class Solution(object):
    def maxProfit(self, prices):
        maxprofit = 0
        
        for y in range(len(prices)):
            for x in range (1, len(prices)):
                if x > y:
                    profit = prices[x] - prices[y]
                    maxprofit = max(maxprofit, profit)


        return maxprofit
#my solution above works but only for small inputs.

#big O notation is how code slows as data grows O stands for order of
# so for O(n) where n is the length of the input, it means that as the input size grows,
#  the time taken grows linearly this is suboptimal for large inputs, this is called linear time complexity.
#O(1) is constant time complexity, meaning the time taken does not change with the size of the input.
"""
        O(n^2) O(n)
        | |   /
        | |  /
        | | /                       O(1) = constant time complexity
   TIME | |/_____________O(log n)   O(n) = linear time complexity
        | /                         O(n^2) = quadratic time complexity
        |/                          O(n log n) = quasilinear time complexity
        |---------------O(1)        O(n^2) = quadratic time complexity
        -------------------
                DATA(n)
"""

#so to fix this we need to right the function using constant time complexity

class Solution(object):
    def maxProfit(self, prices):
        maxprofit = 0
        minprice = float('inf')
        for price in prices:
            if price < minprice:
                minprice = price
            elif price - minprice > maxprofit:
                maxprofit = price - minprice



        return maxprofit