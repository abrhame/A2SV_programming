class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = float("inf")
        # print(nums)
        if n <= 4:
            return 0
        
        for i in range(4):
            ans = min(ans,(nums[-1-i]-nums[3-i]))
        return ans