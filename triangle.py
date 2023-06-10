class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # problem: find the minumum path from the top of the triangle to the bottom of the triangle, you can move from the top to the next level onnly through either i + 1 or i
        # approach: start from the last traingle and find the smallest eleemnt that can lead to the current eleement. and the first element would be the minimum path that lead to top from the bottom

        # time complexity: O(n^2)
        # space complexity: O(len(triangle[len(triangle)-1]))

        n = len(triangle)
        dp = triangle[-1]

        for i in range(n-2,-1,-1):
            for j in range(i+1):
                dp[j] = triangle[i][j] + min(dp[j],dp[j+1])
        print(dp)
        return dp[0]