class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        max_ = float('-inf')
        s = 0
        for r in range(len(nums)):
            s += nums[r]
            if r - l == k - 1:
                max_= max(s/k,max_)
                s -= nums[l]
                l += 1
        return max_
            