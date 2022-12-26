class Solution:
    def canJump(self, nums: List[int]) -> bool:
            maximum = 0
            for i in range(len(nums)):
                    if i > maximum:
                        return False
                    maximum = max(maximum, i + nums[i])
            return True
    
    