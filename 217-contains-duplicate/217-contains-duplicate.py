class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_ = {}
        for i in range(len(nums)):
            if nums[i] in set_:
                return True
            else:
                set_[nums[i]] = True
        return False
            