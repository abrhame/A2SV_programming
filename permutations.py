class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = []
        bitmask = 0

        def backtrack(current):
            nonlocal bitmask
            if len(current) == len(nums):
                perm.append(current)
                return
            
            for i in range(len(nums)):
                if (bitmask >> i) & 1 == 0:
                    bitmask |= 1 << i
                    backtrack(current + [nums[i]])
                    bitmask ^= 1 << i
            
        backtrack([])
        return perm