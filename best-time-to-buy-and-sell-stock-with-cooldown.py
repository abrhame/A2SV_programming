class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0
        
        buy = [0] * n
        profit = [0] * n
        buy[0] = -prices[0]
        
        for i in range(1, n):
            buy[i] = max(buy[i-1], profit[i-2] - prices[i])
            profit[i] = max(profit[i-1], buy[i-1] + prices[i])
        print(buy)
        print(profit)
        return profit[-1]