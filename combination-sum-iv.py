class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        def solve(target,nums,cur,dp):
            if cur == target:
                return 1
            
            if cur > target:
                return 0

            if cur in dp:
                return dp[cur]

            ans = 0 
            for num in nums:
                ans += solve(target, nums, cur + num, dp)
            
            dp[cur] = ans
            return ans
        
        return solve(target, nums,0,{})