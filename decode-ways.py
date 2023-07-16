class Solution:
    def numDecodings(self, s: str) -> int:
        # approach there are two ways to calculate the number of letters we get at the n. the first is chking the validity of the single digit and the second is chcking the validity of the the two digits
        # time complextiy: O(n)
        #space complexity: O(n)
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1

        if s[0] != '0':
            dp[1] = 1

        for i in range(2, n + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[n]