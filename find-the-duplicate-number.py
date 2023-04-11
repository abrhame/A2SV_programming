class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            if nums[nums[i] - 1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != i + 1:
                return nums[i]