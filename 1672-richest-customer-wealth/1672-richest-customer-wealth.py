class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for customer in accounts:
            total = 0
            for wealth in customer:
                total += wealth
            richest = max(richest, total)
        return richest