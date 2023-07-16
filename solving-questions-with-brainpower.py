class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        dp[-1] = questions[-1][0]

        for i in range(n-2, -1, -1):
            dp[i] = questions[i][0]
            jump = questions[i][1]

            if i + jump + 1 < n:
                dp[i] += dp[i + jump + 1]
            
            # make dp[i] if you solve it or if you skip it
            dp[i] = max(dp[i],dp[i+1])
        
        return dp[0]