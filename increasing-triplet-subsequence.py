class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        n = len(nums)
        x = float("inf")
        y = -float("inf")

        for i in range(n):
            if x < y < nums[i]:
                return True
            if nums[i] < x:
                x = nums[i]
            elif nums[i] > x:
                y = nums[i]
        return False