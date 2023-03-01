class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        prefix = [0] * n
        odd = 0
        for i in range(n):
            prefix[odd] += 1
            
            if nums[i] % 2 != 0:
                odd += 1
            if odd >= k:
                count += prefix[odd-k]
        return count
                
            
            