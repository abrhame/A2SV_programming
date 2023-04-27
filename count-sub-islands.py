class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        visited = set()
        count = 0
        flag = True
        def inbound(i,j):
            return (0 <= i < len(grid2)) and (0 <= j < len(grid2[0]))

        def solve(i,j):
            nonlocal flag
            directions = [(1,0),(0,1),(0,-1),(-1,0)]
            visited.add((i,j))
            for x,y in directions:
                n_i = i + x
                n_j = j + y
                
                if (n_i,n_j) not in visited and inbound(n_i,n_j) and grid2[n_i][n_j] == 1:
                    if grid1[n_i][n_j] == 0:
                        flag = False
                    solve(n_i,n_j)
                    
                    
            return flag

        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] and (i, j) not in visited:
                    flag = True
                    if not grid1[i][j]:
                        continue
                    solve(i, j)
                    if flag:
                        count += 1
        
        return count