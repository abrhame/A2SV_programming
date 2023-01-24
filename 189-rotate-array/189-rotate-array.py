class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(k):
            p1 = 0
            p2 = len(nums) - 1
            # insert the last element to the zero index and remove it from the nums
            nums.insert(p1, nums[p2])
            nums.pop()
            
        return nums
        
#         for i in range(k):
#             p1 = len(nums) - 2
#             p2 = len(nums) - 1
#             while p1 != -1:
#                 nums[p2], nums[p1] = nums[p1], nums[p2]
#                 p2 -= 1
#                 p1 -= 1
#         return nums


        
        