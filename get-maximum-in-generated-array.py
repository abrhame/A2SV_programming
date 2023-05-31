class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0] * (n + 1)
        nums[0] = 0
        if n > 0:
            nums[1] = 1

        for i in range(2, n + 1):
            nums[i] = nums[i // 2] + (nums[i // 2 + 1] if i % 2 else 0)

        return max(nums)