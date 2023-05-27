class Solution:
    def tribonacci(self, n: int) -> int:
        def solve(n,memo = {}):
            if n in memo: return memo[n]
            if n <= 1:
                return n
            if n == 2:
                return 1
            
            memo[n] = solve(n-1) + solve(n-2) + solve(n-3)
            return memo[n]

        return solve(n)