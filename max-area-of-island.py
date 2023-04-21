class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        area = 0
        
        def inbound(i,j):
            n = len(grid)
            m = len(grid[0])
            return (0 <= i < n) and (0 <= j < m)
        
        def dfs(i,j,count):
            directions = [(1,0),(0,1), (-1,0), (0,-1)]
            for x, y in directions:
                n_i = i + x
                n_j = j + y
                if inbound(n_i,n_j) and grid[n_i][n_j] == 1 and (n_i,n_j) not in visited:     
                    visited.add((n_i,n_j))
                    count = dfs(n_i,n_j,count+1)
            
            return count

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    visited.add((i,j))
                    area = max(area,dfs(i,j,1))
        return area