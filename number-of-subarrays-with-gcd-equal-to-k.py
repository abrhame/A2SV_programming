class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b,a%b)
        for i,val in enumerate(nums):
            for j in range(i,n):
                val = gcd(val,nums[j])
                if val == k:
                    count += 1
                elif val < k:
                    break

        return count