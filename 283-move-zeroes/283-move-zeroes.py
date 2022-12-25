class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # use two pointer iterate over the arr and swap the elements
        # for i in range(len(nums)):
        #     if i+1< len(nums) and nums[i] == 0:
        #         if nums[i+1]!=0:
        #             nums[i],nums[i+1] = nums[i+1],nums[i]
        #         if i+2< len(nums) and nums[i+2] == 0:
        #             nums[i],nums[i+2] = nums[i+2],nums[i]
        #     else:
        #         continue
        # return nums
       	
        i = 0
        for num in range(len(nums)):
            if nums[num] != 0:
                nums[i],nums[num] = nums[num],nums[i]
                i+=1