class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*n for i in range(m)]
        grid[0][0] = 1
        def inbound(i,j):
            return (0 <= i < m) and (0<= j < n)
        for i in range(m):
            for j in range(n):
                if inbound(i-1,j):
                    print(i-1,j)
                    grid[i][j] += grid[i-1][j]
                if inbound(i,j-1):
                    grid[i][j] += grid[i][j-1]
        return grid[m-1][n-1]