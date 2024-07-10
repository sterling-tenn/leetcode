class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        max_p = 0
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                max_p = max(max_p, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
            
        return max_p