class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]

        
        count = [0] * k
        count[0] = 1 
        ans = 0

        for i in range(len(nums)):
            mod = nums[i] % k
            ans += count[mod]
            count[mod] += 1

        return ans

        