class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        
        p1 = 0
        p2 = 0
        
        
        while p2 < len(nums):
            if nums[p2] != 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 +=1
            p2+=1
        
        
        
#         p2 = 1
        
#         while p2 < len(nums) and p1<len(nums):
#             if nums[p1] != 0:
#                 p1 += 1
#             elif nums[p2] == 0:
#                 p2+=1
#             elif nums[p2] != 0 and nums[p1] == 0:
#                 nums[p1], nums[p2] = nums[p2], nums[p1]
#                 p1+=1
#                 p2+=1

        
#         p = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[p] = nums[i]
#                 p = p+1
#         for i in range(p,len(nums)):
#             nums[i] = 0
#         return nums
        
            
            
            
       