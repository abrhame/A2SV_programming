class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                nums[i-1] = nums[i-1] * 2
                nums[i] = 0
            
        p = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[p] = nums[i]
                p = p + 1
        for i in range(p,len(nums)):
            nums[i] = 0
        
        return nums

    