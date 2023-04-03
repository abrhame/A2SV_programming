class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        total = 1
        ans = set()
        
        for num in nums:
            total *= num
        for i,val in enumerate(nums):
            d = 2
            while d * d <= val:
                while val % d == 0:
                    ans.add(d)
                    val //= d
                d += 1
            if val > 1:
                ans.add(val)
            # print(ans)
        return len(ans)