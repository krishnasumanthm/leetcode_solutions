class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0 or len(prices) == 1:
            return 0
        max_diff = prices[1] - prices[0]
        min_element = prices[0]
        for i in xrange(len(prices)):
            if prices[i]-min_element > max_diff:
                max_diff = prices[i]-min_element
            if prices[i] < min_element:
                min_element = prices[i]
        return max_diff