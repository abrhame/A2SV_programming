class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # min_price = float('inf')
        # max_profit = 0
        
        # for i in range(n):
        #     min_price = min(min_price,prices[i])
        #     max_profit = max(max_profit, prices[i] - min_price)

        # return max_profit
        @cache
        def sell(k):
            if k<0:
                return float("inf"),0
            min_p,max_p=sell(k-1)
            return min(min_p,prices[k]),max(max_p,prices[k]-min_p)
        mini,maxi=sell(n-1)
        return maxi

        