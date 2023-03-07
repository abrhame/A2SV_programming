class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        ans = []
        while l < r+1:
            if nums[l] == target:
                ans.append(l)
                break
            l+=1
        while 0 <= r:
            if nums[r] == target:
                ans.append(r)
                break
            r-=1
            
        if len(ans) >1:
            return ans
        else:
            return [-1,-1]