class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
    
        for num in arr:
            if num - difference in dp:
                dp[num] = dp[num - difference] + 1
            else:
                dp[num] = 1
        
        return max(dp.values())