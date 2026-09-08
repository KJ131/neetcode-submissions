class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0 
        for right in range(len(prices)):
            if prices[l] > prices[right]:
                l = right
            profit = max(profit, prices[right] - prices[l])
            
        return profit
