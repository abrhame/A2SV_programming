class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        l = 0 
        r = len(nums) - 1
        count = 0
        while l < r:
            if nums[l] + nums[r] == k:
                count += 1
                nums.pop(r)
                nums.pop(l)
                r -= 2
            elif nums[l] + nums[r] < k:
                l += 1
            else: 
                r -= 1
        return count
        