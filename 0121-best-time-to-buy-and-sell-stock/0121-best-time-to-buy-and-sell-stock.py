class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        
        # two pointers to represent sliding window (buy and sell)
        left, right = 0, 1
        
        while right < len(prices):
            if prices[left] < prices[right]:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                # found a cheaper time to buy
                left = right
            right += 1 # keep looking into the future for a high price to sell
                
        return max_profit