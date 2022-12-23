class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            if sum(nums[i+1:i+3])>nums[i]:
                return sum(nums[i:i+3])
        return 0