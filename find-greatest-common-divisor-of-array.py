class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small = min(nums)
        large = max(nums)
        def gcd(large,small):
            if small == 0:
                return large
            return gcd(small, large % small)
        return gcd(large,small)