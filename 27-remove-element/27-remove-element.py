class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # given nums list
        # iterate over the nums list and if you find val remove the element and 
        # append underscore 
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else: 
                i +=1
        return len(nums)