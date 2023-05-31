class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def solve(amt):
            nonlocal memo
            if amt == 0:
                return 0

            if amt in memo:
                return memo[amt]

            temp = float('inf')
            for i in range(len(coins)):
                val = amt - coins[i]
                if val >= 0:
                    temp = min(temp,solve(val))
            memo[amt] = temp + 1
            return temp + 1

        x = solve(amount)

        return x if x != float('inf') else -1