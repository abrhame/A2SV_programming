class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum_ = 0
        length = float("inf")
        l = 0
        for r in range(len(nums)):
            sum_ += nums[r]
            while sum_ >= target:
                length = min(length, r - l + 1)
                sum_ -= nums[l]
                l += 1

        if length == float('inf'):
            return 0
        else: return length