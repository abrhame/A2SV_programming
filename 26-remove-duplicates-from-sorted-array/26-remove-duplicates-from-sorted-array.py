class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0     # the holder
        p2 = 1     # the seeker
        
        while p2 < len(nums):
            # find the elemnt that is diffrent from the the holder and move it next to the holder
            if nums[p1] != nums[p2]:
                nums[p1+1] = nums[p2]
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        return p1+1