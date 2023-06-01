class Solution:
    def rob(self, nums: List[int]) -> int:
        # find the amount of money you can rob, starting from the first element to the n - 1 and also find the amont of money you can rob starting from the second element to n.
        # find the maximum of the two computations

        if len(nums) == 1:
            return nums[0]
        nums1 = nums[:]
        r1,r2 = 0,0
        for h in range(len(nums)-1):
            temp = max(nums[h]+r1,r2)
            r1 = r2
            r2 = temp
        ans1 = max(r1,r2)
        r1,r2 = 0,0
        for h in range(1,len(nums1)):
            temp = max(nums1[h]+r1,r2)
            r1 = r2
            r2 = temp
        ans2 = max(r1,r2)
        return max(ans1,ans2)