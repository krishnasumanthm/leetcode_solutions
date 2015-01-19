class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0 or len(prices) == 1:
            return 0
        i = 0
        sell_prices = []
        buy_prices = []
        while (i<len(prices)):
            while i<len(prices)-1 and prices[i+1]<=prices[i]:
                i +=1
            buy_prices.append(i)
            i +=1
            while i<len(prices) and prices[i]>=prices[i-1]:
                i +=1
            sell_prices.append(i-1)
        profit = 0
        for j in xrange(len(sell_prices)):
            profit = profit + prices[sell_prices[j]] - prices[buy_prices[j]]
        return profit