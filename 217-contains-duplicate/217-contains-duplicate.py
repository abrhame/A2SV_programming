class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_ =set()
        for num in nums:
            if num in set_:
                return True
            else:
                set_.add(num)
        return False
            