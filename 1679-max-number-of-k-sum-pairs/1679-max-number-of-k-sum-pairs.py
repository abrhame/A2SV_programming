class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # sort the array to move the pointers easily with condtion
        nums.sort()
        
        l = 0 
        r = len(nums) - 1
        count = 0
        while l < r:
            # if the sum of the two pointers gives the target remove them and increment the count
            if nums[l] + nums[r] == k:
                count += 1
                nums.pop(r)
                nums.pop(l)
                r -= 2
            # if the sum is less than the target move the left pointer to the right
            elif nums[l] + nums[r] < k:
                l += 1
            # if the sum is larger than the target move the right pointer to the left
            else: 
                r -= 1
        return count
        