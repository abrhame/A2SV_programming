class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # richest = 0
        # for customer in accounts:
        #     total = 0
        #     for wealth in customer:
        #         total += wealth
        #     if total > richest:
        #         richest = total
        # return richest
        
        wealth = []
        
        for value in accounts:
            wealth.append(sum(value))
        return max(wealth)
        