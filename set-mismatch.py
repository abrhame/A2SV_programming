class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        i = 0
        while i < n:
            if 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                j = nums[i] -1
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                res.append(nums[i])
                res.append(i+1)
        return res