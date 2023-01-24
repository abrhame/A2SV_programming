class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        # two pointer(seeker and holder)
        p1 = 0          # this is the holder index. which holds the the postion of the zero
        p2 = 0      # this is the seeker. which holds the postion of the non zero variable
        
        
        while p2 < len(nums):      
            # if there is a non zero element, swap it with the zeros element
            if nums[p2] != 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 +=1
            p2+=1
            
            
            
       
