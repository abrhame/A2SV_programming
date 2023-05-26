class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        smallest = nums[0]
        move = 3
        for i in range(n-1,-1,-1):
            if move == 0:
                break
            if nums[i] != smallest:
                nums[i] = smallest
                move -= 1
        # print(nums)
        return max(nums) - min(nums)