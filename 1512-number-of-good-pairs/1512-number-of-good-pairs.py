class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    count+=1
                else:
                    continue
        return count