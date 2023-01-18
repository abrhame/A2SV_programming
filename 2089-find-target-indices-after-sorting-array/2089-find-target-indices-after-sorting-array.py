class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # sort the array
        nums.sort()
        
        # find the target in the nums. append the index of the target
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        return res
        
        