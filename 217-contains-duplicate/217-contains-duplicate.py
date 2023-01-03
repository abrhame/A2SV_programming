class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_ = {}
        for num in nums:
            if num in set_:
                return True
            else:
                set_[num] = True
        return False
            