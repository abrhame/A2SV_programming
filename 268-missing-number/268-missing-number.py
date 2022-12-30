class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set_ = set()
        for num in nums:
            set_.add(num)
        for i in range(len(nums) + 1):
            if i not in set_:
                return i
            else:
                continue

        