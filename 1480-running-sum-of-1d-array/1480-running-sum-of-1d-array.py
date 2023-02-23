class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        sum_ = 0
        for num in nums:
            sum_ += num
            res.append(sum_)
        return res