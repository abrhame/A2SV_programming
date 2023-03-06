class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 < x:
                ans = mid
                left = mid + 1
            elif mid ** 2 > x:
                right = mid - 1
            else:
                ans = mid
                break
        return ans